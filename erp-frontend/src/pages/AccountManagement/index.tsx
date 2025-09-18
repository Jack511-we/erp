import React, { useEffect, useState } from 'react';

declare global {
  interface Window {
    selectedAccount?: string;
    selectedCountry?: string;
  }
}

// 假设后端接口为 /api/kpi-summary，参数有 account, country, timeType, timeValue
// 返回字段如：[{ date: '2025-09-01', sales: 12345 }, ...]

const AccountKpiTable: React.FC = () => {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [timeType, setTimeType] = useState('day'); // 日/周/月/季/半年/年
  const [timeValue, setTimeValue] = useState('2025-09-01'); // 默认时间，可根据实际需求调整

  // 账号和国家可以从全局变量或props获取
  const account = window.selectedAccount || 'owosald';
  const country = window.selectedCountry || 'US';

  useEffect(() => {
    setLoading(true);
    setError('');
    // 构造请求参数
    const params = new URLSearchParams({
      account,
      country,
      timeType,
      timeValue,
    });
    fetch(`/api/kpi-summary?${params.toString()}`)
      .then(res => res.json())
      .then(res => {
        if (res.code === 0 && Array.isArray(res.data)) {
          setData(res.data);
        } else {
          setError(res.message || '数据获取失败');
        }
      })
      .catch(() => setError('网络错误或后端服务异常'))
      .finally(() => setLoading(false));
  }, [account, country, timeType, timeValue]);

  return (
    <div style={{ padding: '24px' }}>
      <h2>销售数据聚合表</h2>
      <div style={{ marginBottom: 16 }}>
        <label>时间类型：</label>
        <select value={timeType} onChange={e => setTimeType(e.target.value)}>
          <option value="day">日</option>
          <option value="week">周</option>
          <option value="month">月</option>
          <option value="quarter">季</option>
          <option value="halfyear">半年</option>
          <option value="year">年</option>
        </select>
        <label style={{ marginLeft: 16 }}>时间：</label>
        <input type="text" value={timeValue} onChange={e => setTimeValue(e.target.value)} style={{ width: 120 }} />
      </div>
      {loading ? <div>加载中...</div> : error ? <div style={{ color: 'red' }}>{error}</div> : (
        <table border={1} cellPadding={8} style={{ width: '100%', borderCollapse: 'collapse' }}>
          <thead>
            <tr>
              <th>时间</th>
              <th>销售额</th>
              {/* 可根据实际需求添加更多字段 */}
            </tr>
          </thead>
          <tbody>
            {data.length === 0 ? (
              <tr><td colSpan={2}>暂无数据</td></tr>
            ) : (
              data.map((row: any, idx: number) => (
                <tr key={idx}>
                  <td>{row.date || row.period}</td>
                  <td>{row.sales}</td>
                </tr>
              ))
            )}
          </tbody>
        </table>
      )}
    </div>
  );
};

export default AccountKpiTable;
