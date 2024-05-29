/*
 *  Copyright 2018 TWO SIGMA OPEN SOURCE, LLC
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

import { BeakerXDataGrid } from '../BeakerXDataGrid';
import { ColumnManager } from '../column/ColumnManager';
import { BeakerXDataStore } from '../store/BeakerXDataStore';
import { createModalTemplate } from './columnLimitModalTemplate';

export class ColumnLimitModal {
  store: BeakerXDataStore;
  columnManager: ColumnManager;
  container: HTMLElement;
  modalId: string;

  constructor(dataGrid: BeakerXDataGrid, container: HTMLElement) {
    this.store = dataGrid.store;
    this.columnManager = dataGrid.columnManager;
    this.container = container;
    this.modalId = dataGrid.id;

    this.init();
  }

  shouldOpenModal() {
    return this.store.selectOutputColumnLimit() < this.store.selectColumnNames().length;
  }

  init() {
    if (!this.shouldOpenModal()) {
      return;
    }

    const modal = document.createElement('div');

    modal.id = this.modalId;
    modal.style.display = 'none';
    modal.innerHTML = createModalTemplate(
      this.store.selectOutputColumnLimit(),
      this.store.selectColumnNames().length,
    );

    this.container.appendChild(modal);
    this.bindEvents(modal);

    setTimeout(() => {
      modal.style.display = 'block';
    });
  }

  bindEvents(modal) {
    const buttons = modal.querySelectorAll('button') || [];

    buttons[0].addEventListener('mouseup', (e) => {
      this.container.removeChild(modal);
      this.columnManager.indexColumns[0].menu.open(e, 1);
    });
    buttons[1].addEventListener('mouseup', () => this.container.removeChild(modal));
  }
}
