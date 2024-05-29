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

import { expect } from 'chai';
import { BeakerXDataGrid } from "../../../src/dataGrid/BeakerXDataGrid";
import { DataGridColumn } from "../../../src/dataGrid/column/DataGridColumn";
import { UniqueEntriesHighlighter } from "../../../src/dataGrid/highlighter/UniqueEntriesHighlighter";
import { HIGHLIGHTER_TYPE } from "../../../src/dataGrid/interface/IHighlighterState";
import { createStore } from "../../../src/dataGrid/store/BeakerXDataStore";
import {
  cellConfigMock,
  columnOptionsMock,
  highlighterStateMock,
  modelStateMock,
  tableDisplayWidgetMock
} from "../mock";

describe('UniqueEntriesHighlighter', () => {
  const dataStore = createStore({ ...modelStateMock, types: ['double', 'double']});
  const dataGrid = new BeakerXDataGrid({}, dataStore, tableDisplayWidgetMock as any);
  const column = new DataGridColumn(
    columnOptionsMock,
    dataGrid,
    dataGrid.columnManager
  );

  let uniqueEntriesHighlighter = new UniqueEntriesHighlighter(
    column,
    { ...highlighterStateMock, type: HIGHLIGHTER_TYPE.uniqueEntries }
  );

  it('should be an instance of highlighter', () => {
    expect(uniqueEntriesHighlighter).to.be.an.instanceof(UniqueEntriesHighlighter);
  });

  it('should have the getBackgroundColor method', () => {
    expect(uniqueEntriesHighlighter).to.have.property('getBackgroundColor');
  });

  it('should have the midColor state property', () => {
    expect(uniqueEntriesHighlighter.state).to.have.property('colors');
  });

  it('should return proper backgroud color', () => {
    expect(uniqueEntriesHighlighter.getBackgroundColor(cellConfigMock))
      .to.include('85%, 85%)');
    expect(uniqueEntriesHighlighter.getBackgroundColor({ ...cellConfigMock, value: 0 }))
      .to.include('85%, 85%)');
    expect(uniqueEntriesHighlighter.getBackgroundColor({ ...cellConfigMock, value: 0.5 }))
      .to.equal('');
  });
});
