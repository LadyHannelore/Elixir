const tocList = document.getElementById('tocList');
const backToTop = document.getElementById('backToTop');
const sectionHeadings = Array.from(document.querySelectorAll('main article h2'));

const charts = [
  {
    id: 'chart-digital-disconnect',
    type: 'bar',
    data: {
      labels: ['Marketing Budget Consumed', 'Total Revenue Generated'],
      datasets: [
        {
          label: 'Percentage',
          data: [25, 5],
          backgroundColor: ['#1b3a60', '#457b9d'],
          borderColor: ['#1b3a60', '#457b9d'],
          borderWidth: 1,
          borderRadius: 10,
        },
      ],
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: { display: false },
        title: {
          display: false,
        },
      },
      scales: {
        y: {
          beginAtZero: true,
          max: 30,
          ticks: {
            stepSize: 5,
          },
        },
      },
    },
  },
  {
    id: 'chart-ai-growth',
    type: 'line',
    data: {
      labels: ['2026', '2027', '2028', '2029', '2030', '2031'],
      datasets: [
        {
          label: 'AI Retail Market Size ($B)',
          data: [18.64, 25.03, 33.57, 45.00, 60.34, 81.54],
          borderColor: '#1b3a60',
          backgroundColor: 'rgba(69, 123, 157, 0.25)',
          fill: true,
          tension: 0.35,
          pointRadius: 5,
          pointHoverRadius: 7,
        },
      ],
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: { display: false },
        title: { display: false },
      },
      scales: {
        x: { grid: { display: false } },
        y: {
          beginAtZero: false,
          ticks: {
            callback: (value) => `$${value}B`,
          },
        },
      },
    },
  },
  {
    id: 'chart-strategic-matrix',
    type: 'bar',
    data: {
      labels: ['Full Omnichannel', 'Flagship Plus', 'B2B Pivot', 'Platform-First'],
      datasets: [
        {
          label: 'Customer Impact',
          data: [22, 18, 10, 12],
          backgroundColor: '#1b3a60',
        },
        {
          label: 'Strategic Alignment',
          data: [20, 18, 5, 15],
          backgroundColor: '#457b9d',
        },
        {
          label: 'Implementation Risk',
          data: [10, 15, 18, 18],
          backgroundColor: '#a8dadc',
        },
        {
          label: 'TCO',
          data: [12, 16, 15, 15],
          backgroundColor: '#e63946',
        },
        {
          label: 'Scalability',
          data: [15, 8, 12, 10],
          backgroundColor: '#f1faee',
          borderColor: '#6c7a89',
          borderWidth: 1,
        },
      ],
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: { position: 'top' },
      },
      scales: {
        x: {
          stacked: true,
          grid: { display: false },
        },
        y: {
          stacked: true,
          beginAtZero: true,
          max: 100,
        },
      },
    },
  },
];

function buildTableOfContents() {
  if (!tocList || sectionHeadings.length === 0) {
    return;
  }

  sectionHeadings.forEach((heading) => {
    const id = heading.id || heading.textContent.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/(^-|-$)/g, '');
    heading.id = id;

    const listItem = document.createElement('li');
    const button = document.createElement('button');
    button.type = 'button';
    button.textContent = heading.textContent;
    button.addEventListener('click', () => {
      document.getElementById(id).scrollIntoView({ behavior: 'smooth', block: 'start' });
    });

    listItem.appendChild(button);
    tocList.appendChild(listItem);
  });
}

function updateActiveToc() {
  const offset = window.innerHeight * 0.25;
  let activeId = sectionHeadings[0]?.id;

  sectionHeadings.forEach((heading) => {
    const rect = heading.getBoundingClientRect();
    if (rect.top <= offset) {
      activeId = heading.id;
    }
  });

  document.querySelectorAll('#tocList button').forEach((button) => {
    button.classList.toggle('active', button.textContent === document.getElementById(activeId)?.textContent);
  });
}

function updateScrollButton() {
  if (!backToTop) {
    return;
  }

  backToTop.style.display = window.scrollY > 450 ? 'flex' : 'none';
}

function renderCharts() {
  if (typeof Chart === 'undefined') {
    return;
  }

  charts.forEach((chartConfig) => {
    const canvas = document.getElementById(chartConfig.id);
    if (!canvas) {
      return;
    }
    new Chart(canvas, {
      type: chartConfig.type,
      data: chartConfig.data,
      options: chartConfig.options,
    });
  });
}

function init() {
  buildTableOfContents();
  updateActiveToc();
  updateScrollButton();
  renderCharts();

  window.addEventListener('scroll', () => {
    updateActiveToc();
    updateScrollButton();
  });

  if (backToTop) {
    backToTop.addEventListener('click', () => {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }
}

document.addEventListener('DOMContentLoaded', init);
