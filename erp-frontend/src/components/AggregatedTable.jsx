import React, { useEffect, useState } from 'react';
import { ReactTabulator } from 'react-tabulator';
import 'react-tabulator/lib/styles.css';
import 'tabulator-tables/dist/css/tabulator.min.css';


// 表格字段定义（与后端聚合文件一致）
const columns = [
  { title: '日期', field: 'date', width: 180, formatter: cell => cell.getValue() ? new Date(cell.getValue()).toLocaleString() : '' },
  { title: '销售额', field: 'sales', hozAlign: 'right', width: 120 },
];

export default function AggregatedTable({ account, year, month, filename }) {
  const [data, setData] = useState([]);
  useEffect(() => {
    if (!account || !year || !month || !filename) return;
    fetch(`/api/aggregated/${account}/${year}/${month}/${filename}`)
      .then(res => res.json())
      .then(json => {
        console.log('后端聚合接口返回数据:', json);
        setData(json.data || []);
      });
  }, [account, year, month, filename]);

  return (
    <div>
      <h2>日汇总表格（自动聚合结果展示）</h2>
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
