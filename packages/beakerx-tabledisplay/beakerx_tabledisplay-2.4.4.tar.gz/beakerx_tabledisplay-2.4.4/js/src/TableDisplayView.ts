/*
 *  Copyright 2017 TWO SIGMA OPEN SOURCE, LLC
 *
 *  Licensed under the Apache License, Version 2.0 (the "License");
 *  you may not use this file except in compliance with the License.
 *  You may obtain a copy of the License at
 *
 *         http://www.apache.org/licenses/LICENSE-2.0
 *
 *  Unless required by applicable law or agreed to in writing, software
 *  distributed under the License is distributed on an "AS IS" BASIS,
 *  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 *  See the License for the specific language governing permissions and
 *  limitations under the License.
 */

import * as widgets from '@jupyter-widgets/base';
import { DataGridScope } from './dataGrid';
import { TableDisplayWidget } from './TableDisplayWidget';

export class TableDisplayView extends widgets.DOMWidgetView implements TableDisplayWidget {
  private _currentScope: DataGridScope;

  render(): void {
    this._currentScope = null;
    this.$el.addClass('beaker-table-display');

    this.displayed.then(() => {
      const tableModel = this.model.get('model');

      if (tableModel.tooManyRows) {
        this.showWarning(tableModel);
      }

      this.initDataGridTable(tableModel);

      this.listenTo(this.model, 'beakerx-tabSelected', () => {
        this._currentScope?.setInitialSize();
      });

      this.listenTo(this.model, 'change:updateData', this.handleUpdateData);
      this.listenTo(this.model, 'change:model', this.handleModelUpdate);
    });
  }

  protected get currentScope(): DataGridScope {
    return this._currentScope;
  }

  handleModelUpdate(model, value, options): void {
    let shouldReset = options.shouldResetModel==undefined || options.shouldResetModel;
    if (shouldReset){
      this._currentScope.doResetAll();
      this._currentScope.updateModelData(this.model.get('model'));
    }
  }
  handleUpdateData(model, value, options): void {
    const change = this.model.get('updateData');
    const currentModel = this.model.get('model');
    if (change.hasOwnProperty('values')){
      this.updateValues(currentModel, change);
    }else {
      this.model.set('model', {...currentModel, ...change});
      this.handleModelUpdate(model,value, options);
    }
  }

  private updateValues(currentModel, change) {
    let newValues = currentModel.values.concat(change.values || [])
    let newFonts = currentModel.fontColor;
    if (change.hasOwnProperty('fontColor')) {
      newFonts = currentModel.fontColor.concat(change.fontColor || [])
    }
    this.model.set('model', {
      ...currentModel, ...change,
      values: newValues,
      fontColor: newFonts
    }, {"shouldResetModel": false});
    this._currentScope.updateModelValues(this.model.get('model'));
    this.model.set('loadMoreRows', "loadMoreJSDone");
  }

  showWarning(data): void {
    const rowLimitMsg = data.rowLimitMsg;
    const modal = document.createElement('div');

    modal.innerHTML = `<p class="ansired">${rowLimitMsg}</p>`;

    this.el.appendChild(modal);
  }

  initDataGridTable(data: any): void {
    this._currentScope = new DataGridScope({
      element: this.el,
      data: data,
      widgetModel: this.model,
      widgetView: this,
    });

    this._currentScope.render();
  }

  remove(): void {
    this._currentScope && this._currentScope.doDestroy();

    if (this.pWidget) {
      this.pWidget.dispose();
    }

    this._currentScope = null;

    return super.remove.call(this);
  }

  canLoadMore(): boolean {
    return (
      this.isEndlessLoadingMode() &&
      (this.model.get('loadMoreRows') == 'loadMoreServerInit' || this.model.get('loadMoreRows') == 'loadMoreJSDone')
    );
  }

  loadMoreRows(): void {
    this.model.set('loadMoreRows', 'loadMoreRequestJS');
    this.touch();
  }

  private isEndlessLoadingMode(): boolean {
    return this.model.get('model').loadingMode == 'ENDLESS';
  }
}
