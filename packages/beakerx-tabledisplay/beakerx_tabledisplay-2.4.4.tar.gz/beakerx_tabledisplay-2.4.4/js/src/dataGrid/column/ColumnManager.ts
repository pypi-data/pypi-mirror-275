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

import { chain, find } from '@lumino/algorithm';
import { CellRenderer, DataModel } from '@lumino/datagrid';
import { Signal } from '@lumino/signaling';
import { BeakerXDataGrid } from '../BeakerXDataGrid';
import { DataGridHelpers } from '../Helpers';
import { ICellData } from '../interface/ICell';
import { IColumnPosition, IColumns } from '../interface/IColumn';
import { RESET_COLUMNS_ORDER, UPDATE_COLUMNS_VISIBLE } from '../model/BeakerXDataGridModel';
import { BeakerXDataStore } from '../store/BeakerXDataStore';
import { DataGridAction, DataGridColumnsAction } from '../store/DataGridAction';
import { DataGridColumn } from './DataGridColumn';
import { COLUMN_TYPES, SORT_ORDER } from './enums';
import { UPDATE_COLUMNS_FILTERS } from '../store/BeakerXDataStore';

export interface IBkoColumnsChangedArgs {
  type: COLUMN_CHANGED_TYPES;
  value: any;
  column: DataGridColumn;
}

export enum COLUMN_CHANGED_TYPES {
  'columnSort',
}

export class ColumnManager {
  store: BeakerXDataStore;
  dataGrid: BeakerXDataGrid;
  columns: IColumns = {};
  columnsChanged = new Signal<this, IBkoColumnsChangedArgs>(this);

  constructor(dataGrid: BeakerXDataGrid) {
    this.dataGrid = dataGrid;
    this.store = this.dataGrid.store;
  }

  static createPositionFromCell(config: CellRenderer.CellConfig | ICellData): IColumnPosition {
    const region = ColumnManager.getColumnRegionByCell(config);

    return { region, value: config.column };
  }

  static getColumnRegionByCell(
    config: CellRenderer.CellConfig | ICellData | { region: DataModel.CellRegion },
  ): DataModel.ColumnRegion {
    return config.region === 'row-header' || config.region === 'corner-header' ? 'row-header' : 'body';
  }

  get bodyColumns() {
    return this.columns[COLUMN_TYPES.body];
  }

  get indexColumns() {
    return this.columns[COLUMN_TYPES.index];
  }

  get bodyColumnNames(): string[] {
    return this.store.selectBodyColumnNames();
  }

  get indexColumnNames(): string[] {
    return this.store.selectIndexColumnNames();
  }

  addColumns() {
    this.createColumnsMap();
    this.addIndexColumns();
    this.addBodyColumns();
  }

  getColumn(config: CellRenderer.CellConfig): DataGridColumn {
    const columnType = DataGridColumn.getColumnTypeByRegion(config.region, config.column);
    const columnIndex = this.store.selectColumnIndexByPosition(ColumnManager.createPositionFromCell(config));

    return this.columns[columnType][columnIndex];
  }

  getColumnByIndex(columnType: COLUMN_TYPES, index: number) {
    return this.columns[columnType][index];
  }

  getColumnByPosition(position: IColumnPosition) {
    return this.dataGrid.columnPosition.getColumnByPosition(position);
  }

  getColumnByName(columnName: string): DataGridColumn | undefined {
    return find(chain(this.bodyColumns, this.indexColumns), (column: DataGridColumn) => column.name === columnName);
  }

  destroy(): void {
    this.destroyAllColumns();
    Signal.disconnectAll(this);
  }

  sortByColumn(column: DataGridColumn, sortOrder: SORT_ORDER) {
    this.columnsChanged.emit({
      column,
      type: COLUMN_CHANGED_TYPES.columnSort,
      value: sortOrder,
    });
    this.dataGrid.rowManager.sortByColumn(column);
    this.dataGrid.dataModel.reset();
  }

  resetFilters() {
    const resetFilterFn = (column) => column.columnFilter.hideInput();

    this.store.dispatch(
      new DataGridColumnsAction(UPDATE_COLUMNS_FILTERS, {
        hasIndex: this.store.selectHasIndex(),
        value: this.store.selectColumnNames().map(() => ''),
        defaultValue: [''],
      }),
    );
    this.dataGrid.dataModel.setFilterHeaderVisible(false);
    this.bodyColumns.forEach(resetFilterFn);
    this.indexColumns.forEach(resetFilterFn);
    this.dataGrid.rowManager.filterRows();
  }

  showFilters(column?: DataGridColumn) {
    this.showFilterInputs(false, column);
  }

  showSearch(column?: DataGridColumn) {
    this.showFilterInputs(true, column);
  }

  blurColumnFilterInputs() {
    this.bodyColumns.forEach((column) => column.columnFilter.blur());
    this.indexColumns.forEach((column) => column.columnFilter.blur());
  }

  updateColumnFilterNodes() {
    this.bodyColumns.forEach((column) => column.columnFilter.updateInputNode(false));
    this.indexColumns.forEach((column) => column.columnFilter.updateInputNode(false));
  }

  updateColumnMenuTriggers() {
    this.bodyColumns.forEach((column) => column.menu && column.menu.updateTriggerPosition());
    this.indexColumns.forEach((column) => column.menu && column.menu.updateTriggerPosition());
  }

  closeAllMenus() {
    this.bodyColumns.forEach((column) => column.menu && column.menu.close());
    this.indexColumns.forEach((column) => column.menu && column.menu.close());
  }

  takeColumnsByCells(startCell: ICellData, endCell: ICellData) {
    let result: any[] = [];

    if (endCell.type !== COLUMN_TYPES.index) {
      result = this.bodyColumns
        .filter((column) => {
          const position = column.getPosition();

          if (!column.getVisible()) {
            return false;
          }

          if (startCell.region === endCell.region) {
            return position.value >= startCell.column && position.value <= endCell.column;
          }

          return (
            (position.region === 'row-header' && position.value >= startCell.column) ||
            (position.region === 'body' && position.value <= endCell.column)
          );
        })
        .sort(DataGridHelpers.sortColumnsByPositionCallback);
    }

    if (startCell.type === COLUMN_TYPES.index) {
      result.unshift(this.indexColumns[0]);
    }

    return result;
  }

  takeColumnByCell(cellData: ICellData): DataGridColumn | null {
    const column = this.getColumnByPosition(ColumnManager.createPositionFromCell(cellData));

    return column ? column : null;
  }

  showAllColumns() {
    const columnNames = this.store.selectColumnNames();
    const hasIndex = this.store.selectHasIndex();

    this.store.dispatch(
      new DataGridColumnsAction(UPDATE_COLUMNS_VISIBLE, {
        hasIndex,
        value: columnNames.reduce((acc, name) => {
          acc[name] = true;
          return acc;
        }, {}),
        defaultValue: [0],
      }),
    );

    this.store.dispatch(new DataGridAction(RESET_COLUMNS_ORDER, { value: false }));
    this.dataGrid.columnPosition.updateAll();
  }

  resetColumnsAlignment() {
    this.bodyColumns.forEach((column) => {
      column.resetAlignment();
    });
    this.dataGrid.dataModel.reset();
  }

  resetColumnPositions() {
    this.dataGrid.columnPosition.reset();
  }

  resetColumnStates() {
    this.indexColumns.forEach((column) => column.resetState());
    this.bodyColumns.forEach((column) => column.resetState());
  }

  restoreColumnStates() {
    this.indexColumns.forEach((column) => column.restoreState());
    this.bodyColumns.forEach((column) => column.restoreState());
  }

  setColumnsDataTypePrecission(precission: number) {
    this.indexColumns.forEach((column) => column.setDataTypePrecision(precission));
    this.bodyColumns.forEach((column) => column.setDataTypePrecision(precission));
  }

  recalculateMinMaxValues() {
    this.recalculateColumnsMinMax(this.bodyColumns);
    this.recalculateColumnsMinMax(this.indexColumns);
  }

  createColumnMenus() {
    this.indexColumns.forEach((column) => column.createMenu());
    this.bodyColumns.forEach((column) => column.createMenu());
  }

  private recalculateColumnsMinMax(columns: DataGridColumn[]) {
    columns.forEach((column) => {
      column.addMinMaxValues();
    });
  }

  private showFilterInputs(useSearch: boolean, column?: DataGridColumn) {
    const methodToCall = useSearch ? 'showSearchInput' : 'showFilterInput';
    const showInputsFn = (columnItem) => {
      const position = columnItem.getPosition();

      columnItem.columnFilter[methodToCall](
        column === columnItem,
        this.dataGrid.getColumnOffset(position.value, position.region),
      );
    };

    this.dataGrid.dataModel.setFilterHeaderVisible(true);
    this.bodyColumns.forEach(showInputsFn);
    this.indexColumns.forEach(showInputsFn);
  }

  private addBodyColumns() {
    this.store.selectBodyColumnNames().forEach((name, index) => this.addColumn(name, index, COLUMN_TYPES.body));
  }

  private addIndexColumns(): void {
    this.store.selectIndexColumnNames().forEach((name, index) => this.addColumn(name, index, COLUMN_TYPES.index));
  }

  private addColumn(name, index, type) {
    const column = new DataGridColumn(
      {
        name,
        index,
        type,
      },
      this.dataGrid,
      this,
    );

    this.columns[type].push(column);
  }

  private createColumnsMap() {
    const bodyColumns: DataGridColumn[] = [];
    const indexColumns: DataGridColumn[] = [];

    this.columns[COLUMN_TYPES.index] = indexColumns;
    this.columns[COLUMN_TYPES.body] = bodyColumns;
  }

  private destroyAllColumns() {
    this.indexColumns.forEach((column: DataGridColumn) => column.destroy());
    this.bodyColumns.forEach((column: DataGridColumn) => column.destroy());

    this.createColumnsMap();

    Signal.disconnectAll(this);
  }
}
