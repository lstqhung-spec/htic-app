module.exports = Object.assign({
      darkMode: "class",
      theme: {
        extend: {
          colors: {
            "htic-primary": "#243e8f",
            "htic-accent": "#0f71b9",
            "htic-neutral": "#f2f2f3",
            "htic-dark": "#16285c",
            "primary": "#243e8f",
            "primary-container": "#1d3274",
            "secondary": "#0f71b9",
            "background": "#ffffff",
            "surface": "#ffffff",
            "surface-container-low": "#f2f2f3",
            "surface-container": "#e8eaf1",
            "surface-card": "#ffffff",
            "text-primary": "#111827",
            "text-secondary": "#4b5563",
            "text-muted": "#6b7280",
            "border-subtle": "#e5e7eb",
            "on-primary": "#ffffff"
          },
          borderRadius: {
            "DEFAULT": "0.25rem",
            "lg": "0.5rem",
            "xl": "0.75rem",
            "2xl": "1rem",
            "full": "9999px"
          },
          spacing: {
            "space-3xl": "6rem",
            "space-sm": "0.5rem",
            "margin": "3rem",
            "space-2xl": "4rem",
            "gutter-mobile": "1rem",
            "space-xl": "2.5rem",
            "space-xs": "0.25rem",
            "space-lg": "1.5rem",
            "gutter": "1.5rem",
            "space-md": "1rem",
            "margin-mobile": "1.25rem"
          },
          fontFamily: {
            sans: ["Plus Jakarta Sans", "system-ui", "-apple-system", "sans-serif"],
            "headline-lg": ["Plus Jakarta Sans", "sans-serif"],
            "label-caps": ["Plus Jakarta Sans", "sans-serif"],
            "body-lead": ["Plus Jakarta Sans", "sans-serif"],
            "metric-num": ["Plus Jakarta Sans", "sans-serif"],
            "body-default": ["Plus Jakarta Sans", "sans-serif"],
            "headline-md": ["Plus Jakarta Sans", "sans-serif"],
            "headline-xl": ["Plus Jakarta Sans", "sans-serif"],
            "button-text": ["Plus Jakarta Sans", "sans-serif"],
            "display-hero": ["Plus Jakarta Sans", "sans-serif"],
            "body-sm": ["Plus Jakarta Sans", "sans-serif"],
            "headline-sm": ["Plus Jakarta Sans", "sans-serif"]
          },
          fontSize: {
            "headline-lg": ["32px", { lineHeight: "40px", letterSpacing: "-0.015em", fontWeight: "700" }],
            "label-caps": ["11px", { lineHeight: "16px", letterSpacing: "0.08em", fontWeight: "700" }],
            "body-lead": ["18px", { lineHeight: "28px", fontWeight: "400" }],
            "display-hero-mobile": ["34px", { lineHeight: "42px", letterSpacing: "-0.02em", fontWeight: "800" }],
            "metric-num": ["36px", { lineHeight: "40px", letterSpacing: "-0.02em", fontWeight: "800" }],
            "body-default": ["15px", { lineHeight: "24px", fontWeight: "400" }],
            "headline-md": ["24px", { lineHeight: "32px", letterSpacing: "-0.01em", fontWeight: "700" }],
            "headline-xl-mobile": ["28px", { lineHeight: "36px", letterSpacing: "-0.015em", fontWeight: "700" }],
            "headline-xl": ["38px", { lineHeight: "48px", letterSpacing: "-0.02em", fontWeight: "800" }],
            "button-text": ["14px", { lineHeight: "20px", letterSpacing: "0.01em", fontWeight: "600" }],
            "display-hero": ["52px", { lineHeight: "62px", letterSpacing: "-0.025em", fontWeight: "800" }],
            "body-sm": ["13px", { lineHeight: "20px", fontWeight: "400" }],
            "headline-sm": ["18px", { lineHeight: "26px", fontWeight: "700" }]
          }
        }
      }
    },{content:['/home/claude/htic-app/hticlaw-site/index.html','/home/claude/htic-app/hticlaw-site/*/index.html','/home/claude/htic-app/hticlaw-site/*/*/index.html'],plugins:[require('@tailwindcss/forms'),require('@tailwindcss/container-queries')]});
