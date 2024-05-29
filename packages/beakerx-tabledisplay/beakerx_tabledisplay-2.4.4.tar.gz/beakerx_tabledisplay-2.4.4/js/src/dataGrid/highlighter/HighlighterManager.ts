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

import { each, filter, toArray } from '@lumino/algorithm';
import { CellRenderer } from '@lumino/datagrid';
import { Theme } from '../../utils/Theme';
import { BeakerXDataGrid } from '../BeakerXDataGrid';
import { DataGridColumn } from '../column/DataGridColumn';
import { HIGHLIGHTER_STYLE, HIGHLIGHTER_TYPE, IHighlighterState } from '../interface/IHighlighterState';
import { ADD_COLUMN_HIGHLIGHTER, REMOVE_COLUMN_HIGHLIGHTER } from '../model/BeakerXDataGridModel';
// import { selectCellHighlighters } from '../model/selectors/model';
import { DataGridColumnAction } from '../store/DataGridAction';
import { Highlighter } from './Highlighter';
import { HighlighterFactory } from './HighlighterFactory';

export class HighlighterManager {
  highlighters: Highlighter[];
  dataGrid: BeakerXDataGrid;
  cachedHighlighters: Map<string, Highlighter>;

  constructor(dataGrid: BeakerXDataGrid) {
    this.dataGrid = dataGrid;
    this.highlighters = [];
    this.cachedHighlighters = new Map<string, Highlighter>();

    this.createHighlighter = this.createHighlighter.bind(this);
    this.registerHighlighter = this.registerHighlighter.bind(this);
    this.unregisterHighlighter = this.unregisterHighlighter.bind(this);

    this.createHighlighters();
  }

  destroy(): void {
    this.dataGrid = null;
    this.highlighters = [];
    this.cachedHighlighters.forEach((highlighter) => highlighter.destroy());
    this.cachedHighlighters.clear();
  }

  createHighlighters() {
    const state = this.dataGrid.store.selectCellHighlighters();

    state.forEach(this.createHighlighter);
  }

  createHighlighter(state: IHighlighterState): void {
    const column = this.dataGrid.getColumnByName(state.colName);

    if (!column) {
      return;
    }

    const highlighter = this.cachedHighlighters.get(this.getHighlighterKey(column, state.type));

    if (highlighter) {
      return this.registerHighlighter(highlighter);
    }

    this.registerHighlighter(HighlighterFactory.getHighlighter(state, column));
  }

  registerHighlighter(highlighter: Highlighter | null) {
    if (!highlighter) {
      throw new Error(`Can not register highlighter: ${highlighter}`);
    }

    if (highlighter.state.type === HIGHLIGHTER_TYPE.sort) {
      this.highlighters.unshift(highlighter);
    } else {
      this.highlighters.push(highlighter);
      this.cachedHighlighters.set(this.getHighlighterKey(highlighter.column, highlighter.state.type), highlighter);
    }
  }

  unregisterHighlighter(highlighter: Highlighter) {
    const index = this.highlighters.indexOf(highlighter);

    if (index !== -1) {
      this.highlighters.splice(index, 1);
    }
  }

  getColumnHighlighters(column, highlighterType?: HIGHLIGHTER_TYPE): Highlighter[] {
    return toArray(
      filter(this.highlighters, (highlighter: Highlighter) => {
        return highlighterType
          ? highlighter.column === column && highlighter.state.type === highlighterType
          : highlighter.column === column;
      }),
    );
  }

  addColumnHighlighter(column, highlighterType: HIGHLIGHTER_TYPE) {
    const highlighterState = this.createColumnHighlighterState(highlighterType, column);
    this.registerHighlighter(
      this.cachedHighlighters.get(this.getHighlighterKey(column, highlighterType)) ||
        HighlighterFactory.getHighlighter(highlighterState, column),
    );
  }

  updatedColumnHighlighter(column, highlighterType: HIGHLIGHTER_TYPE) {
    const highlighterState = this.createColumnHighlighterState(highlighterType, column);
    this.registerHighlighter(HighlighterFactory.getHighlighter(highlighterState, column));
  }

  private createColumnHighlighterState(highlighterType: HIGHLIGHTER_TYPE, column) {
    const highlighterState: IHighlighterState = {
      ...HighlighterFactory.defaultHighlighterState,
      type: highlighterType,
      minVal: column.minValue,
      maxVal: column.maxValue,
      colName: column.name,
    };
    this.removeColumnHighlighter(column, highlighterType);
    this.dataGrid.store.dispatch(
      new DataGridColumnAction(ADD_COLUMN_HIGHLIGHTER, {
        columnIndex: column.index,
        columnName: column.name,
        value: highlighterState,
      }),
    );
    return highlighterState;
  }

  restoreHighlighters(column, highlighterType?: HIGHLIGHTER_TYPE) {
    const highlighters = this.getColumnHighlighters(column, highlighterType);
    highlighters.forEach((value) => this.updatedColumnHighlighter(column, value.state.type));
  }

  removeColumnHighlighter(column, highlighterType?: HIGHLIGHTER_TYPE) {
    const highlighters = this.getColumnHighlighters(column, highlighterType);

    each(highlighters, (highlighter) => {
      this.dataGrid.store.dispatch(
        new DataGridColumnAction(REMOVE_COLUMN_HIGHLIGHTER, {
          value: highlighter.state,
          columnName: column.name,
          columnIndex: column.index,
        }),
      );
      this.unregisterHighlighter(highlighter);
    });
  }

  toggleColumnHighlighter(column, highlighterType: HIGHLIGHTER_TYPE) {
    if (this.getColumnHighlighters(column, highlighterType).length) {
      this.removeColumnHighlighter(column, highlighterType);
    } else {
      this.addColumnHighlighter(column, highlighterType);
    }

    this.dataGrid.repaintBody();
  }

  removeHighlighters() {
    this.highlighters.splice(0, this.highlighters.length);
    this.dataGrid.repaintBody();
  }

  getCellBackground(config: CellRenderer.CellConfig): string {
    let background = Theme.DEFAULT_COLOR;
    const column = this.dataGrid.getColumn(config);

    each(this.highlighters, (highlighter: Highlighter) => {
      if (highlighter.column === column || highlighter.state.style === HIGHLIGHTER_STYLE.FULL_ROW) {
        background = highlighter.getBackgroundColor(config);
      }
    });

    return background;
  }

  private getHighlighterKey(column: DataGridColumn, highlighterType: string): string {
    return `${column.index}_${column.type}_${highlighterType}`;
  }
}
