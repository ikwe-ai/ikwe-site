(function () {
  var SAMPLE_PAGE_MAP = {
    '/downloads/ikwe_public_preview.pdf': '/samples/public-preview.html',
    '/downloads/ikwe_board_brief.pdf': '/samples/board-brief.html',
    '/downloads/ikwe_audit_report.pdf': '/samples/audit-report.html',
    '/downloads/ikwe_scorecard_sample.pdf': '/samples/public-preview.html#scorecard',
    '/downloads/ikwe_report_sample.pdf': '/samples/board-brief.html#report',
    '/downloads/ikwe_action_plan_sample.pdf': '/samples/audit-report.html#action-plan'
  };

  function samplePreviewUrlFor(href) {
    try {
      var abs = new URL(href, window.location.origin);
      var pathname = abs.pathname.toLowerCase();
      var mapped = SAMPLE_PAGE_MAP[pathname];
      if (!mapped) return null;
      return new URL(mapped, window.location.origin).href;
    } catch (e) {
      return null;
    }
  }

  function isSamplePdfLink(a) {
    if (!a || !a.getAttribute) return false;
    var href = a.getAttribute('href') || '';
    return href.indexOf('/downloads/') === 0 && href.toLowerCase().endsWith('.pdf');
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
      '      <a class="sample-preview-btn" id="sample-preview-view" href="#" target="_blank" rel="noopener">View PDF</a>',
      '      <a class="sample-preview-btn" id="sample-preview-download" href="#" download>Download PDF</a>',
      '      <a class="sample-preview-btn" id="sample-preview-email" href="#">Send to myself</a>',
      '      <button class="sample-preview-close" id="sample-preview-close" type="button" aria-label="Close">×</button>',
      '    </div>',
      '  </div>',
      '  <div class="sample-preview-frame-wrap">',
      '    <iframe class="sample-preview-frame" id="sample-preview-frame" title="Sample preview"></iframe>',
      '    <div class="sample-preview-note">Preview keeps you on-page. Use buttons for full PDF actions.</div>',
      '    <div class="sample-preview-fallback hidden" id="sample-preview-fallback">',
      '      Live preview unavailable for this file. Use View PDF or Download PDF.',
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
    var frame = document.getElementById('sample-preview-frame');
    var titleEl = document.getElementById('sample-preview-title');
    var viewBtn = document.getElementById('sample-preview-view');
    var downloadBtn = document.getElementById('sample-preview-download');
    var emailBtn = document.getElementById('sample-preview-email');
    var closeBtn = document.getElementById('sample-preview-close');
    var fallback = document.getElementById('sample-preview-fallback');

    function closeModal() {
      modal.classList.remove('is-open');
      modal.setAttribute('aria-hidden', 'true');
      document.documentElement.style.overflow = '';
      frame.removeAttribute('src');
    }

    function openModal(href, title) {
      var abs = new URL(href, window.location.origin).href;
      var previewUrl = samplePreviewUrlFor(href) || abs;
      titleEl.textContent = title || 'Sample Preview';
      fallback.classList.add('hidden');
      frame.src = previewUrl;
      viewBtn.href = abs;
      downloadBtn.href = abs;
      var subject = encodeURIComponent('Ikwe sample: ' + (title || 'PDF sample'));
      var body = encodeURIComponent('Here is the Ikwe sample PDF:\n\n' + abs);
      emailBtn.href = 'mailto:?subject=' + subject + '&body=' + body;
      modal.classList.add('is-open');
      modal.setAttribute('aria-hidden', 'false');
      document.documentElement.style.overflow = 'hidden';
    }

    links.forEach(function (a) {
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
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && modal.classList.contains('is-open')) closeModal();
    });

    frame.addEventListener('error', function () {
      fallback.classList.remove('hidden');
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
