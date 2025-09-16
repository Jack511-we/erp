import React from 'react';
import { ReactTabulator } from 'react-tabulator';
import 'react-tabulator/lib/styles.css'; // Tabulator 样式
import 'tabulator-tables/dist/css/tabulator.min.css'; // Tabulator 样式

// mock 数据
const data = [
  { id: 1, sku: 'A001', name: '商品A', quantity: 120, price: 35 },
  { id: 2, sku: 'B002', name: '商品B', quantity: 80, price: 50 },
  { id: 3, sku: 'C003', name: '商品C', quantity: 200, price: 20 },
];

// 表格字段定义
const columns = [
  { title: 'ID', field: 'id', width: 60 },
  { title: 'SKU', field: 'sku', width: 100 },
  { title: '名称', field: 'name', width: 150 },
  { title: '库存数量', field: 'quantity', hozAlign: 'right', width: 120 },
  { title: '单价', field: 'price', hozAlign: 'right', width: 100 },
];

export default function TabulatorTable() {
  return (
    <div>
      <h2>库存表格（Tabulator 高性能表格）</h2>
      <ReactTabulator
        data={data}
        columns={columns}
        layout="fitData"
        options={{
          movableColumns: true,
          resizableRows: true,
          pagination: true,
          paginationSize: 10,
        }}
      />
    </div>
  );
}
