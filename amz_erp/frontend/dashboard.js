// 仪表盘前端 ECharts 渲染与真实后端接口对接
let currentTheme = null;
async function fetchChartData(module, startDate, endDate) {
    const response = await fetch(`/api/${module}_analysis`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ start_date: startDate, end_date: endDate })
    });
    return await response.json();
}

function renderChart(domId, chartData, chartType, title) {
    var chartDom = document.getElementById(domId);
    var myChart = echarts.init(chartDom, currentTheme);
    var option = {
        title: { text: title, left: 'center', textStyle: { fontFamily: 'Microsoft YaHei', fontWeight: 'bold' } },
        tooltip: {
            trigger: 'axis',
            formatter: function(params) {
                return params.map(p => `${p.seriesName}: ${p.value}`).join('<br>');
            }
        },
        legend: { data: chartData.series.map(s => s.name), top: 30 },
        xAxis: { type: 'category', data: chartData.categories },
        yAxis: { type: 'value' },
        series: chartData.series.map(s => ({
            name: s.name,
            type: chartType,
            data: s.data,
            emphasis: { focus: 'series' },
            label: { show: true, fontFamily: 'Microsoft YaHei' }
        })),
        grid: { left: 40, right: 20, top: 60, bottom: 40 }
    };
    myChart.setOption(option);
    // 图表点击事件，下钻明细
    myChart.on('click', function(params) {
        showDetailModal(params.name, params.value);
    });
    // 导出PNG按钮
    chartDom.insertAdjacentHTML('afterend', `<button id='${domId}_btn' onclick="exportChartPNG('${domId}')">导出图表PNG</button>`);
}

window.exportChartPNG = function(domId) {
    var myChart = echarts.getInstanceByDom(document.getElementById(domId));
    var imgData = myChart.getDataURL({ type: 'png', pixelRatio: 2 });
    var a = document.createElement('a');
    a.href = imgData;
    a.download = domId + '.png';
    a.click();
}

async function renderDashboard(modules, startDate, endDate, sku, adType) {
    // 清空所有图表
    ['orderChart','inventoryChart','adsChart','settlementChart','summaryChart'].forEach(id => {
        document.getElementById(id).innerHTML = '';
        let btn = document.getElementById(id + '_btn');
        if (btn) btn.remove();
    });
    // 批量渲染选中模块图表
    for (const mod of modules) {
        const chartData = await fetchChartData(mod, startDate, endDate);
        let chartType = 'bar';
        if (mod === 'ads') chartType = 'line';
        if (mod === 'inventory') chartType = 'pie';
        renderChart(mod + 'Chart', chartData, chartType, mod + '分析');
    }
}

// 页面加载速度优化：懒加载图表
function lazyLoadCharts(modules, startDate, endDate) {
    modules.forEach((mod, idx) => {
        setTimeout(() => {
            renderDashboard([mod], startDate, endDate);
        }, idx * 300); // 间隔加载，减少首屏压力
    });
}

// 筛选交互（可扩展为下拉/多选）
// ...可在表单中增加维度筛选控件...

// 主题切换
function applyTheme(theme) {
    document.body.className = theme;
    // 可扩展：ECharts主题同步
}
const themeBtn = document.getElementById('themeBtn');
themeBtn.addEventListener('click', function() {
    currentTheme = currentTheme === 'dark' ? null : 'dark';
    applyTheme(currentTheme === 'dark' ? 'dark-theme' : 'light-theme');
    const modules = Array.from(document.getElementById('modules').selectedOptions).map(opt => opt.value);
    const startDate = document.getElementById('startDate').value;
    const endDate = document.getElementById('endDate').value;
    renderDashboard(modules, startDate, endDate);
});

// 多条件筛选与刷新
const refreshBtn = document.getElementById('refreshBtn');
refreshBtn.addEventListener('click', function() {
    const modules = Array.from(document.getElementById('modules').selectedOptions).map(opt => opt.value);
    const startDate = document.getElementById('startDate').value;
    const endDate = document.getElementById('endDate').value;
    const sku = document.getElementById('skuFilter').value;
    const adType = document.getElementById('adType').value;
    // 可扩展：将筛选条件传递给后端
    renderDashboard(modules, startDate, endDate, sku, adType);
});

// 批量导出报表
const batchExportBtn = document.getElementById('batchExportBtn');
batchExportBtn.addEventListener('click', function() {
    showExportProgress('正在生成报表，请稍候...');
    const modules = Array.from(document.getElementById('modules').selectedOptions).map(opt => opt.value);
    const startDate = document.getElementById('startDate').value;
    const endDate = document.getElementById('endDate').value;
    const format = document.getElementById('exportFormat').value;
    // 调用后端批量导出接口
    fetch('/api/batch_export', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ modules, start_date: startDate, end_date: endDate, format })
    })
    .then(res => res.blob())
    .then(blob => {
        const a = document.createElement('a');
        a.href = URL.createObjectURL(blob);
        a.download = `批量报表_${startDate}_${endDate}.${format}`;
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
    })
    .finally(() => {
        showExportProgress('导出完成！');
        // 导出完成后关闭弹窗
        setTimeout(() => { document.getElementById('detailModal').style.display = 'none'; }, 3000);
    });
});

// 图表联动：点击SKU图表，刷新店铺和广告系列图表
function handleChartLinkage(type, value) {
    // type: 'sku' | 'shop' | 'ad'
    // value: 当前点击的值
    // 可扩展：根据type和value刷新相关图表
    if (type === 'sku') {
        // 刷新店铺和广告系列图表
        renderChart('inventoryChart', {/*...根据SKU筛选后的数据...*/}, 'pie', '店铺分布');
        renderChart('adsChart', {/*...根据SKU筛选后的数据...*/}, 'line', '广告系列');
    }
    // ...其他联动逻辑...
}

// 下钻弹窗
function showDetailModal(name, value) {
    const modal = document.getElementById('detailModal');
    modal.innerHTML = `<div class='modal-content'><h3>明细数据</h3><p>名称：${name}</p><p>数值：${value}</p><button onclick="exportDetail('${name}', ${value})">导出明细</button><button onclick="closeModal()">关闭</button></div>`;
    modal.style.display = 'flex';
}
window.closeModal = function() {
    document.getElementById('detailModal').style.display = 'none';
}

// 多级下钻弹窗
function showMultiLevelDetail(level, value) {
    // level: ['sku', 'shop', 'ad']
    // value: 当前点击的值
    const modal = document.getElementById('detailModal');
    let content = `<div class='modal-content'><h3>明细数据（${level.join(' → ')}）</h3>`;
    content += `<p>当前层级：${level[level.length-1]}</p><p>数值：${value}</p>`;
    if (level.length < 3) {
        content += `<button onclick="nextDrill('${level.join(',')}', '${value}')">下钻下一层</button>`;
    }
    content += `<button onclick="exportDetail('${value}', ${value})">导出明细</button><button onclick="closeModal()">关闭</button></div>`;
    modal.innerHTML = content;
    modal.style.display = 'flex';
}
window.nextDrill = function(levelStr, value) {
    // 模拟下钻到下一层
    const levels = levelStr.split(',');
    if (levels.length === 1) {
        showMultiLevelDetail(['sku','shop'], value);
    } else if (levels.length === 2) {
        showMultiLevelDetail(['sku','shop','ad'], value);
    }
}

// 明细导出功能（可扩展为Excel/CSV/PDF）
window.exportDetail = function(name, value) {
    const format = document.getElementById('exportFormat')?.value || 'csv';
    // 可扩展：根据当前下钻层级导出不同明细
    if (format === 'csv') {
        const csv = `名称,数值\n${name},${value}`;
        const blob = new Blob([csv], { type: 'text/csv' });
        const a = document.createElement('a');
        a.href = URL.createObjectURL(blob);
        a.download = '明细数据.csv';
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
    } else {
        // Excel/PDF 由后端生成，前端请求下载
        fetch(`/api/export_detail`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ name, value, format })
        })
        .then(res => res.blob())
        .then(blob => {
            const a = document.createElement('a');
            a.href = URL.createObjectURL(blob);
            a.download = format === 'xlsx' ? '明细数据.xlsx' : '明细数据.pdf';
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
        });
    }
}

// 智能筛选控件：SKU模糊搜索与补全
const skuInput = document.getElementById('skuFilter');
skuInput.addEventListener('input', function() {
    const val = skuInput.value.trim();
    if (val.length > 1) {
        fetch(`/api/sku_suggest?query=${encodeURIComponent(val)}`)
            .then(res => res.json())
            .then(list => {
                // 可用 datalist 或自定义下拉展示
                let datalist = document.getElementById('skuSuggest');
                if (!datalist) {
                    datalist = document.createElement('datalist');
                    datalist.id = 'skuSuggest';
                    skuInput.setAttribute('list', 'skuSuggest');
                    document.body.appendChild(datalist);
                }
                datalist.innerHTML = list.map(sku => `<option value='${sku}'>`).join('');
            });
    }
});

// 筛选控件批量选择优化（模块多选、广告类型多选）
// ...可扩展为多选下拉或标签选择...

// 图表刷新动画与动态提示
function animateChartRefresh(domId) {
    const chartDom = document.getElementById(domId);
    chartDom.classList.add('chart-refresh');
    setTimeout(() => chartDom.classList.remove('chart-refresh'), 600);
}
// 在 renderChart 渲染后调用 animateChartRefresh(domId)

// 导出任务进度反馈
function showExportProgress(msg) {
    const modal = document.getElementById('detailModal');
    modal.innerHTML = `<div class='modal-content'><h3>导出进度</h3><p>${msg}</p></div>`;
    modal.style.display = 'flex';
}
// 批量导出时分步提示
batchExportBtn.addEventListener('click', function() {
    showExportProgress('正在生成报表，请稍候...');
    const modules = Array.from(document.getElementById('modules').selectedOptions).map(opt => opt.value);
    const startDate = document.getElementById('startDate').value;
    const endDate = document.getElementById('endDate').value;
    const format = document.getElementById('exportFormat').value;
    // 调用后端批量导出接口
    fetch('/api/batch_export', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ modules, start_date: startDate, end_date: endDate, format })
    })
    .then(res => res.blob())
    .then(blob => {
        const a = document.createElement('a');
        a.href = URL.createObjectURL(blob);
        a.download = `批量报表_${startDate}_${endDate}.${format}`;
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
    })
    .finally(() => {
        showExportProgress('导出完成！');
        // 导出完成后关闭弹窗
        setTimeout(() => { document.getElementById('detailModal').style.display = 'none'; }, 3000);
    });
});

// 自动生成：筛选组合保存与加载
const saveFilterBtn = document.getElementById('saveFilterBtn');
const loadFilterBtn = document.getElementById('loadFilterBtn');
saveFilterBtn.addEventListener('click', function() {
    const filter = {
        startDate: document.getElementById('startDate').value,
        endDate: document.getElementById('endDate').value,
        modules: Array.from(document.getElementById('modules').selectedOptions).map(opt => opt.value),
        sku: document.getElementById('skuFilter').value,
        adType: Array.from(document.getElementById('adType').selectedOptions).map(opt => opt.value),
        exportFormat: document.getElementById('exportFormat').value
    };
    localStorage.setItem('erp_filter', JSON.stringify(filter));
    alert('筛选组合已保存！');
});
loadFilterBtn.addEventListener('click', function() {
    const filter = JSON.parse(localStorage.getItem('erp_filter') || '{}');
    if (filter.startDate) document.getElementById('startDate').value = filter.startDate;
    if (filter.endDate) document.getElementById('endDate').value = filter.endDate;
    if (filter.modules) {
        Array.from(document.getElementById('modules').options).forEach(opt => {
            opt.selected = filter.modules.includes(opt.value);
        });
    }
    if (filter.sku) document.getElementById('skuFilter').value = filter.sku;
    if (filter.adType) {
        Array.from(document.getElementById('adType').options).forEach(opt => {
            opt.selected = filter.adType.includes(opt.value);
        });
    }
    if (filter.exportFormat) document.getElementById('exportFormat').value = filter.exportFormat;
    alert('筛选组合已加载！');
});

window.onload = function() {
    const modules = ['order','inventory','ads','settlement','summary'];
    lazyLoadCharts(modules, '2025-09-01', '2025-09-15');
};

window.addEventListener('resize', function() {
    ['orderChart','inventoryChart','adsChart','settlementChart','summaryChart'].forEach(id => {
        var myChart = echarts.getInstanceByDom(document.getElementById(id));
        if (myChart) myChart.resize();
    });
});
