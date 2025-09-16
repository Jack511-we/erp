document.getElementById('exportForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    const modules = Array.from(document.getElementById('modules').selectedOptions).map(opt => opt.value);
    const startDate = document.getElementById('startDate').value;
    const endDate = document.getElementById('endDate').value;
    const formats = Array.from(document.querySelectorAll('input[name="format"]:checked')).map(cb => cb.value);
    const resultDiv = document.getElementById('result');
    resultDiv.innerHTML = '<p>正在生成报表，请稍候...</p>';

    // 演示用：模拟后端API调用
    // 实际部署时请替换为真实API接口（如 Flask/FastAPI）
    setTimeout(() => {
        let html = '<h3>报表生成成功</h3>';
        modules.forEach(mod => {
            html += `<b>模块：${mod}</b><ul>`;
            formats.forEach(fmt => {
                // 文件名示例
                let fname = `${mod}_summary_${startDate}_${endDate}.${fmt}`;
                html += `<li><a href='/output/${fname}' download>${fname}</a></li>`;
            });
            html += '</ul>';
        });
        resultDiv.innerHTML = html;
    }, 1200);
});
