(function () {
  var PREVIEW_DATA = {
    '/downloads/ikwe_public_preview.pdf': {
      page: '/samples/public-preview.html',
      image: '/downloads/images/ikwe_public_preview.png',
      summary: 'System Blueprint sample with redacted outputs and baseline findings.',
      cards: ['Scorecard snapshot', 'Risk event framing', 'Mitigation sequence'],
      nextLabel: 'Get DIY Playbook ($5,000)',
      nextHref: 'https://buy.stripe.com/14A5kEbbeetH1cW66B9sk05'
    },
    '/downloads/ikwe_board_brief.pdf': {
      page: '/samples/board-brief.html',
      image: '/downloads/images/ikwe_board_brief.png',
      summary: 'Board-ready brief format for leadership review and decision alignment.',
      cards: ['Posture summary', 'Top exposure paths', 'Action ownership'],
      nextLabel: 'Request Managed Audit ($25,000+)',
      nextHref: '/inquiry'
    },
    '/downloads/ikwe_audit_report.pdf': {
      page: '/samples/audit-report.html',
      image: '/downloads/images/ikwe_audit_report.png',
      summary: 'Full redacted audit report structure with evidence-to-action traceability.',
      cards: ['Dimension scoring', 'Failure mode map', 'Now/Next/Later plan'],
      nextLabel: 'Request Managed Audit ($25,000+)',
      nextHref: '/inquiry'
    },
    '/downloads/ikwe_scorecard_sample.pdf': {
      page: '/samples/public-preview.html#scorecard',
      image: '/downloads/images/ikwe_public_preview.png',
      summary: 'Standalone scorecard sample with baseline and post-mitigation posture.',
      cards: ['Baseline posture', 'Post-mitigation posture', 'Delta interpretation'],
      nextLabel: 'Get DIY Playbook ($5,000)',
      nextHref: 'https://buy.stripe.com/14A5kEbbeetH1cW66B9sk05'
    },
    '/downloads/ikwe_report_sample.pdf': {
      page: '/samples/board-brief.html#report',
      image: '/downloads/images/ikwe_board_brief.png',
      summary: 'Sample report page showing board-facing structure and language.',
      cards: ['Executive readout', 'Evidence block', 'Decision prompt'],
      nextLabel: 'Get DIY Playbook ($5,000)',
      nextHref: 'https://buy.stripe.com/14A5kEbbeetH1cW66B9sk05'
    },
    '/downloads/ikwe_action_plan_sample.pdf': {
      page: '/samples/audit-report.html#action-plan',
      image: '/downloads/images/ikwe_audit_report.png',
      summary: 'Mitigation action plan sample with phased implementation actions.',
      cards: ['Immediate actions', 'Near-term controls', 'Long-term governance'],
      nextLabel: 'Request Managed Audit ($25,000+)',
      nextHref: '/inquiry'
    }
  };

  function keyFor(href) {
    try {
      var abs = new URL(href, window.location.origin);
      return abs.pathname.toLowerCase();
    } catch (e) {
      return '';
    }
  }

  function previewDataFor(href) {
    return PREVIEW_DATA[keyFor(href)] || null;
  }

  var SAMPLE_PAGE_MAP = {
    '/downloads/ikwe_public_preview.pdf': '/samples/public-preview.html',
    '/downloads/ikwe_board_brief.pdf': '/samples/board-brief.html',
    '/downloads/ikwe_audit_report.pdf': '/samples/audit-report.html',
    '/downloads/ikwe_scorecard_sample.pdf': '/samples/public-preview.html#scorecard',
    '/downloads/ikwe_report_sample.pdf': '/samples/board-brief.html#report',
    '/downloads/ikwe_action_plan_sample.pdf': '/samples/audit-report.html#action-plan'
  };

  function samplePreviewUrlFor(href) {
    var data = previewDataFor(href);
    if (data && data.page) return new URL(data.page, window.location.origin).href;
    try {
      var abs = new URL(href, window.location.origin);
      var mapped = SAMPLE_PAGE_MAP[abs.pathname.toLowerCase()];
      if (!mapped) return null;
      return new URL(mapped, window.location.origin).href;
    } catch (e) { return null; }
  }

  function isSamplePdfLink(a) {
    if (!a || !a.getAttribute) return false;
    var href = a.getAttribute('href') || '';
    return href.indexOf('/downloads/') === 0 && href.toLowerCase().endsWith('.pdf');
  }

  function hasMappedSamplePage(href) {
    return !!samplePreviewUrlFor(href);
  }

  function buildModal() {
    var root = document.createElement('div');
    root.className = 'sample-preview-modal';
    root.setAttribute('id', 'sample-preview-modal');
    root.setAttribute('aria-hidden', 'true');
    root.innerHTML = [
      '<div class="sample-preview-backdrop" data-close="1"></div>',
      '<div class="sample-preview-dialog" role="dialog" aria-modal="true" aria-label="Sample preview">',
      '  <div class="sample-preview-head">',
      '    <div class="sample-preview-title" id="sample-preview-title">Sample Preview</div>',
      '    <div class="sample-preview-actions">',
      '      <a class="sample-preview-btn is-primary" id="sample-preview-view" href="#" target="_blank" rel="noopener">Open sample</a>',
      '      <a class="sample-preview-btn" id="sample-preview-download" href="#" download>Get PDF</a>',
      '      <a class="sample-preview-btn" id="sample-preview-next" href="/inquiry">Next step</a>',
      '      <button class="sample-preview-close" id="sample-preview-close" type="button" aria-label="Close">×</button>',
      '    </div>',
      '  </div>',
      '  <div class="sample-preview-frame-wrap">',
      '    <div class="sample-inline-preview" id="sample-inline-preview">',
      '      <div class="sample-inline-media"><img id="sample-preview-image" alt="Sample preview"></div>',
      '      <div class="sample-inline-copy">',
      '        <p class="sample-inline-summary" id="sample-inline-summary"></p>',
      '        <div class="sample-inline-cards" id="sample-inline-cards"></div>',
      '      </div>',
      '    </div>',
      '    <div class="sample-preview-note">Click the preview to open the live sample. Use Get PDF for the downloadable file.</div>',
      '    <div class="sample-preview-fallback hidden" id="sample-preview-fallback">',
      '      Preview unavailable for this file. Use Open sample page or Download PDF.',
      '    </div>',
      '  </div>',
      '</div>'
    ].join('');
    document.body.appendChild(root);
    return root;
  }

  function init() {
    var links = Array.prototype.slice.call(document.querySelectorAll('a[href^="/downloads/"]'))
      .filter(isSamplePdfLink);
    if (!links.length) return;

    var modal = document.getElementById('sample-preview-modal') || buildModal();
    var titleEl = document.getElementById('sample-preview-title');
    var viewBtn = document.getElementById('sample-preview-view');
    var downloadBtn = document.getElementById('sample-preview-download');
    var nextBtn = document.getElementById('sample-preview-next');
    var closeBtn = document.getElementById('sample-preview-close');
    var fallback = document.getElementById('sample-preview-fallback');
    var mediaWrap = document.querySelector('.sample-inline-media');
    var previewImage = document.getElementById('sample-preview-image');
    var summaryEl = document.getElementById('sample-inline-summary');
    var cardsEl = document.getElementById('sample-inline-cards');

    function closeModal() {
      modal.classList.remove('is-open');
      modal.setAttribute('aria-hidden', 'true');
      document.documentElement.style.overflow = '';
      if (previewImage) previewImage.removeAttribute('src');
      if (summaryEl) summaryEl.textContent = '';
      if (cardsEl) cardsEl.innerHTML = '';
    }

    function openModal(href, title) {
      var abs = new URL(href, window.location.origin).href;
      var previewUrl = samplePreviewUrlFor(href);
      if (!previewUrl) return;
      var data = previewDataFor(href);
      titleEl.textContent = title || 'Sample Preview';
      if (data && data.image) {
        previewImage.src = data.image;
        previewImage.alt = (title || 'Sample preview') + ' image';
      } else {
        previewImage.removeAttribute('src');
      }
      summaryEl.textContent = (data && data.summary) ? data.summary : 'Sample output preview.';
      cardsEl.innerHTML = '';
      if (data && data.cards && data.cards.length) {
        data.cards.forEach(function (label) {
          var card = document.createElement('div');
          card.className = 'sample-inline-card';
          card.textContent = label;
          cardsEl.appendChild(card);
        });
      }
      fallback.classList.add('hidden');
      viewBtn.href = previewUrl;
      downloadBtn.href = abs;
      nextBtn.href = (data && data.nextHref) ? data.nextHref : '/inquiry';
      nextBtn.textContent = (data && data.nextLabel) ? data.nextLabel : 'Request Managed Audit ($25,000+)';
      modal.classList.add('is-open');
      modal.setAttribute('aria-hidden', 'false');
      document.documentElement.style.overflow = 'hidden';
    }

    links.forEach(function (a) {
      if (!hasMappedSamplePage(a.getAttribute('href'))) return;
      a.setAttribute('data-sample-preview', '1');
      a.addEventListener('click', function (e) {
        if (e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
        e.preventDefault();
        var t = a.getAttribute('data-title') || a.textContent.trim().replace(/\s+→$/, '');
        openModal(a.getAttribute('href'), t);
      });
    });

    modal.addEventListener('click', function (e) {
      if (e.target && e.target.getAttribute('data-close') === '1') closeModal();
    });
    closeBtn.addEventListener('click', closeModal);
    if (mediaWrap) {
      mediaWrap.addEventListener('click', function () {
        if (viewBtn && viewBtn.href) window.open(viewBtn.href, '_blank', 'noopener');
      });
      mediaWrap.setAttribute('title', 'Open sample');
      mediaWrap.style.cursor = 'pointer';
    }
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && modal.classList.contains('is-open')) closeModal();
    });

    if (previewImage) {
      previewImage.addEventListener('error', function () {
        fallback.classList.remove('hidden');
      });
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
