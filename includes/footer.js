(() => {
  const footerHost = document.getElementById("site-footer");
  if (!footerHost) {
    return;
  }

  const navLinks = window.ikweNavLinks || [
    { href: "/", label: "Home" },
    { href: "/emotional-safety-gap", label: "Findings" },
    { href: "/research", label: "Research" },
    { href: "/research/canon/ai-governance-compliance/", label: "Canon" },
    { href: "/press", label: "Press" },
    { href: "/about", label: "About" },
    { href: "/privacy", label: "Privacy" },
    { href: "/terms", label: "Terms" }
  ];

  const footerLinksMarkup = navLinks
    .map((link) => `<a href="${link.href}" data-path="${link.href}">${link.label}</a>`)
    .concat('<a href="mailto:info@ikwe.ai">Contact</a>')
    .join("");

  footerHost.innerHTML = `
    <footer class="footer">
      <div class="container">
        <div class="footer-inner">
          <div class="footer-brand">ikwe.ai · Visible Healing Inc.</div>
          <nav class="footer-nav">
            ${footerLinksMarkup}
          </nav>
        </div>
      </div>
    </footer>
  `;

  if (window.setIkweActiveLinks) {
    window.setIkweActiveLinks(footerHost);
  }
})();
