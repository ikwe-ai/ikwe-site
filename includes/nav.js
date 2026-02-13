(() => {
  const navHost = document.getElementById("site-nav");
  if (!navHost) {
    return;
  }

  const links = [
    { href: "/", label: "Home" },
    { href: "/emotional-safety-gap", label: "Findings" },
    { href: "/research", label: "Research" },
    { href: "/research/canon/ai-governance-compliance/", label: "Canon" },
    { href: "/press", label: "Press" },
    { href: "/about", label: "About" },
    { href: "/privacy", label: "Privacy" },
    { href: "/terms", label: "Terms" }
  ];

  window.ikweNavLinks = links;

  const navLinksMarkup = links
    .map((link) => `<a href="${link.href}" data-path="${link.href}">${link.label}</a>`)
    .join("");

  navHost.innerHTML = `
    <header class="topbar">
      <div class="container">
        <div class="topbar-inner">
          <a class="brand" href="/"><span class="brand-mark"></span><span>ikwe.ai</span></a>
          <nav class="nav">
            ${navLinksMarkup}
          </nav>
          <div class="nav-cta">
            <a class="btn primary" href="/request-access">Work With Us</a>
          </div>
        </div>
      </div>
    </header>
  `;

  const normalizePath = (path) => {
    if (!path) {
      return "/";
    }

    let normalized = path.replace(/index\.html$/, "").replace(/\.html$/, "");
    if (normalized.length > 1 && normalized.endsWith("/")) {
      normalized = normalized.slice(0, -1);
    }

    return normalized || "/";
  };

  const setActiveLinks = (root = document) => {
    const currentPath = normalizePath(window.location.pathname);
    root.querySelectorAll("[data-path]").forEach((link) => {
      const linkPath = normalizePath(link.dataset.path);
      if (linkPath === currentPath) {
        link.classList.add("active");
      }
    });
  };

  window.setIkweActiveLinks = setActiveLinks;
  setActiveLinks(navHost);
})();
