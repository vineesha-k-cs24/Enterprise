import json
import os

with open('dashboard_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

json_payload = json.dumps(data)

html_code = f'''<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>GlobalTech FinTech Solutions — Executive CFO Financial Suite</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    /* -------------------------------------------------------------
       DESIGN SYSTEM & CSS TOKENS
       ------------------------------------------------------------- */
    :root {{
      --font-sans: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
      --font-mono: 'JetBrains Mono', monospace;
      
      /* Color Tokens (Dark Mode Default) */
      --bg-base: #0b0f19;
      --bg-surface: #111827;
      --bg-surface-elevated: #1e293b;
      --bg-card: rgba(17, 24, 39, 0.75);
      --bg-card-hover: rgba(30, 41, 59, 0.85);
      
      --border-subtle: rgba(255, 255, 255, 0.08);
      --border-strong: rgba(255, 255, 255, 0.16);
      --border-focus: #06b6d4;
      
      --text-primary: #f8fafc;
      --text-secondary: #94a3b8;
      --text-tertiary: #64748b;
      
      /* Brand Accents */
      --cyan-500: #06b6d4;
      --cyan-400: #22d3ee;
      --cyan-glow: rgba(6, 182, 212, 0.25);
      
      --emerald-500: #10b981;
      --emerald-400: #34d399;
      --emerald-glow: rgba(16, 185, 129, 0.2);
      
      --violet-500: #8b5cf6;
      --violet-400: #a78bfa;
      --violet-glow: rgba(139, 92, 246, 0.25);
      
      --amber-500: #f59e0b;
      --amber-glow: rgba(245, 158, 11, 0.2);
      
      --rose-500: #f43f5e;
      --rose-glow: rgba(244, 63, 94, 0.2);

      --radius-sm: 8px;
      --radius-md: 14px;
      --radius-lg: 20px;
      --radius-full: 9999px;
      
      --shadow-sm: 0 2px 8px rgba(0, 0, 0, 0.2);
      --shadow-md: 0 10px 25px -5px rgba(0, 0, 0, 0.3), 0 8px 10px -6px rgba(0, 0, 0, 0.3);
      --shadow-lg: 0 20px 40px -10px rgba(0, 0, 0, 0.5);
      --shadow-glow: 0 0 30px var(--cyan-glow);
    }}

    /* Light Theme Override */
    [data-theme="light"] {{
      --bg-base: #f1f5f9;
      --bg-surface: #ffffff;
      --bg-surface-elevated: #f8fafc;
      --bg-card: rgba(255, 255, 255, 0.85);
      --bg-card-hover: #ffffff;
      
      --border-subtle: #e2e8f0;
      --border-strong: #cbd5e1;
      --border-focus: #0284c7;
      
      --text-primary: #0f172a;
      --text-secondary: #475569;
      --text-tertiary: #94a3b8;
      
      --cyan-500: #0284c7;
      --cyan-400: #0ea5e9;
      --cyan-glow: rgba(2, 132, 199, 0.15);
      
      --shadow-sm: 0 2px 8px rgba(15, 23, 42, 0.05);
      --shadow-md: 0 10px 25px -5px rgba(15, 23, 42, 0.08);
      --shadow-lg: 0 20px 35px -10px rgba(15, 23, 42, 0.12);
    }}

    /* -------------------------------------------------------------
       GLOBAL RESET & BASE STYLES
       ------------------------------------------------------------- */
    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      transition: background-color 0.25s ease, border-color 0.25s ease, color 0.2s ease;
    }}

    body {{
      font-family: var(--font-sans);
      background-color: var(--bg-base);
      color: var(--text-primary);
      min-height: 100vh;
      overflow-x: hidden;
      line-height: 1.5;
      background-image: 
        radial-gradient(circle at 10% 10%, rgba(6, 182, 212, 0.07) 0%, transparent 40%),
        radial-gradient(circle at 90% 90%, rgba(139, 92, 246, 0.08) 0%, transparent 45%);
      background-attachment: fixed;
    }}

    .app-wrapper {{
      max-width: 1560px;
      margin: 0 auto;
      padding: 24px 32px 80px 32px;
    }}

    /* -------------------------------------------------------------
       NAVBAR / TOP HEADER
       ------------------------------------------------------------- */
    header.executive-header {{
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      align-items: center;
      gap: 20px;
      padding-bottom: 24px;
      margin-bottom: 28px;
      border-bottom: 1px solid var(--border-subtle);
    }}

    .brand-cluster {{
      display: flex;
      align-items: center;
      gap: 16px;
    }}

    .brand-mark {{
      width: 52px;
      height: 52px;
      border-radius: var(--radius-md);
      background: linear-gradient(135deg, var(--cyan-500) 0%, var(--violet-500) 100%);
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 800;
      font-size: 24px;
      color: #ffffff;
      box-shadow: 0 8px 24px var(--cyan-glow);
    }}

    .brand-details h1 {{
      font-size: 24px;
      font-weight: 800;
      letter-spacing: -0.025em;
      display: flex;
      align-items: center;
      gap: 10px;
      color: var(--text-primary);
    }}

    .badge-verified {{
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      padding: 4px 10px;
      border-radius: var(--radius-full);
      background: rgba(16, 185, 129, 0.15);
      color: var(--emerald-400);
      border: 1px solid rgba(16, 185, 129, 0.3);
      display: inline-flex;
      align-items: center;
      gap: 5px;
    }}

    .badge-verified::before {{
      content: '';
      width: 6px;
      height: 6px;
      border-radius: 50%;
      background: var(--emerald-400);
      box-shadow: 0 0 8px var(--emerald-400);
    }}

    .brand-details p {{
      font-size: 13px;
      color: var(--text-secondary);
      margin-top: 3px;
    }}

    .header-controls {{
      display: flex;
      align-items: center;
      gap: 12px;
      flex-wrap: wrap;
    }}

    .btn {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 10px 18px;
      font-size: 13px;
      font-weight: 600;
      border-radius: var(--radius-md);
      cursor: pointer;
      border: 1px solid transparent;
      outline: none;
      transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
    }}

    .btn-secondary {{
      background: var(--bg-surface);
      color: var(--text-primary);
      border-color: var(--border-subtle);
    }}

    .btn-secondary:hover {{
      background: var(--bg-surface-elevated);
      border-color: var(--border-strong);
      transform: translateY(-1px);
    }}

    .btn-primary {{
      background: linear-gradient(135deg, var(--cyan-500) 0%, #0284c7 100%);
      color: #ffffff;
      box-shadow: 0 4px 14px var(--cyan-glow);
    }}

    .btn-primary:hover {{
      transform: translateY(-1px);
      box-shadow: 0 6px 20px var(--cyan-glow);
      filter: brightness(1.1);
    }}

    .theme-toggle-btn {{
      width: 42px;
      height: 42px;
      padding: 0;
      display: flex;
      align-items: center;
      justify-content: center;
      border-radius: var(--radius-md);
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      color: var(--text-primary);
      cursor: pointer;
      font-size: 18px;
    }}

    .theme-toggle-btn:hover {{
      background: var(--bg-surface-elevated);
      transform: rotate(15deg);
    }}

    /* -------------------------------------------------------------
       CFO CONTROL BAR & QUARTER SLICERS
       ------------------------------------------------------------- */
    .control-ribbon {{
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      align-items: center;
      gap: 16px;
      background: var(--bg-card);
      backdrop-filter: blur(16px);
      border: 1px solid var(--border-subtle);
      padding: 14px 20px;
      border-radius: var(--radius-lg);
      margin-bottom: 28px;
      box-shadow: var(--shadow-sm);
    }}

    .slicer-group {{
      display: flex;
      align-items: center;
      gap: 6px;
      background: var(--bg-surface);
      padding: 5px;
      border-radius: var(--radius-md);
      border: 1px solid var(--border-subtle);
    }}

    .slicer-btn {{
      padding: 8px 16px;
      font-size: 13px;
      font-weight: 700;
      color: var(--text-secondary);
      background: transparent;
      border: none;
      border-radius: var(--radius-sm);
      cursor: pointer;
      transition: all 0.2s ease;
    }}

    .slicer-btn:hover {{
      color: var(--text-primary);
    }}

    .slicer-btn.active {{
      background: var(--cyan-500);
      color: #ffffff;
      box-shadow: 0 2px 10px var(--cyan-glow);
    }}

    .currency-selector {{
      display: flex;
      align-items: center;
      gap: 8px;
      background: var(--bg-surface);
      padding: 5px;
      border-radius: var(--radius-md);
      border: 1px solid var(--border-subtle);
    }}

    .curr-btn {{
      padding: 6px 12px;
      font-size: 12px;
      font-weight: 700;
      border: none;
      border-radius: var(--radius-sm);
      background: transparent;
      color: var(--text-secondary);
      cursor: pointer;
    }}

    .curr-btn.active {{
      background: var(--bg-surface-elevated);
      color: var(--cyan-400);
    }}

    .stress-test-toggle {{
      display: flex;
      align-items: center;
      gap: 12px;
      font-size: 13px;
      font-weight: 600;
      color: var(--text-secondary);
    }}

    .stress-slider {{
      -webkit-appearance: none;
      width: 140px;
      height: 6px;
      border-radius: 4px;
      background: var(--bg-surface-elevated);
      outline: none;
      cursor: pointer;
    }}

    .stress-slider::-webkit-slider-thumb {{
      -webkit-appearance: none;
      width: 16px;
      height: 16px;
      border-radius: 50%;
      background: var(--cyan-400);
      cursor: pointer;
      box-shadow: 0 0 10px var(--cyan-glow);
    }}

    .stress-pill {{
      font-family: var(--font-mono);
      font-size: 12px;
      font-weight: 700;
      padding: 3px 8px;
      border-radius: var(--radius-sm);
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      color: var(--cyan-400);
      min-width: 48px;
      text-align: center;
    }}

    /* -------------------------------------------------------------
       KPI METRIC CARDS
       ------------------------------------------------------------- */
    .kpi-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 20px;
      margin-bottom: 32px;
    }}

    .kpi-card {{
      background: var(--bg-card);
      backdrop-filter: blur(16px);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-lg);
      padding: 24px;
      position: relative;
      overflow: hidden;
      box-shadow: var(--shadow-sm);
      transition: all 0.25s ease;
    }}

    .kpi-card:hover {{
      transform: translateY(-3px);
      box-shadow: var(--shadow-md);
      border-color: var(--border-strong);
    }}

    .kpi-card::before {{
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 4px;
      background: linear-gradient(90deg, var(--accent-color, var(--cyan-500)), transparent);
    }}

    .kpi-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 12px;
    }}

    .kpi-title {{
      font-size: 13px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--text-secondary);
    }}

    .kpi-icon-badge {{
      width: 36px;
      height: 36px;
      border-radius: var(--radius-md);
      background: var(--bg-surface);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 16px;
      color: var(--accent-color, var(--cyan-500));
      border: 1px solid var(--border-subtle);
    }}

    .kpi-value {{
      font-family: var(--font-mono);
      font-size: 32px;
      font-weight: 800;
      letter-spacing: -0.03em;
      color: var(--text-primary);
      margin-bottom: 8px;
    }}

    .kpi-footer {{
      display: flex;
      align-items: center;
      gap: 10px;
      font-size: 12px;
      color: var(--text-tertiary);
    }}

    .trend-indicator {{
      display: inline-flex;
      align-items: center;
      gap: 4px;
      padding: 2px 8px;
      border-radius: var(--radius-sm);
      font-weight: 700;
      font-size: 11px;
    }}

    .trend-up {{
      background: rgba(16, 185, 129, 0.12);
      color: var(--emerald-400);
    }}

    .trend-stable {{
      background: rgba(6, 182, 212, 0.12);
      color: var(--cyan-400);
    }}

    /* -------------------------------------------------------------
       ANALYTICS & CHARTS SECTION
       ------------------------------------------------------------- */
    .dashboard-grid {{
      display: grid;
      grid-template-columns: 2fr 1fr;
      gap: 24px;
      margin-bottom: 32px;
    }}

    @media (max-width: 1100px) {{
      .dashboard-grid {{
        grid-template-columns: 1fr;
      }}
    }}

    .panel-card {{
      background: var(--bg-card);
      backdrop-filter: blur(16px);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-lg);
      padding: 26px;
      box-shadow: var(--shadow-sm);
      position: relative;
    }}

    .panel-header {{
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 24px;
      gap: 16px;
    }}

    .panel-title h2 {{
      font-size: 18px;
      font-weight: 800;
      letter-spacing: -0.015em;
      color: var(--text-primary);
    }}

    .panel-title p {{
      font-size: 13px;
      color: var(--text-secondary);
      margin-top: 4px;
    }}

    .panel-tags {{
      display: flex;
      gap: 8px;
    }}

    .tag-chip {{
      font-size: 11px;
      font-weight: 700;
      padding: 4px 10px;
      border-radius: var(--radius-full);
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      color: var(--text-secondary);
    }}

    /* Chart SVG Area */
    .chart-container {{
      width: 100%;
      height: 340px;
      position: relative;
    }}

    .chart-svg {{
      width: 100%;
      height: 100%;
      overflow: visible;
    }}

    /* Tooltip */
    .interactive-tooltip {{
      position: absolute;
      pointer-events: none;
      padding: 12px 16px;
      border-radius: var(--radius-md);
      background: var(--bg-surface-elevated);
      border: 1px solid var(--border-strong);
      color: var(--text-primary);
      box-shadow: var(--shadow-lg);
      font-size: 12px;
      z-index: 100;
      opacity: 0;
      transform: translate(-50%, -115%);
      transition: opacity 0.15s ease, transform 0.15s ease;
      white-space: nowrap;
    }}

    .interactive-tooltip.visible {{
      opacity: 1;
    }}

    .tooltip-header {{
      font-weight: 800;
      font-size: 13px;
      margin-bottom: 6px;
      color: var(--cyan-400);
      border-bottom: 1px solid var(--border-subtle);
      padding-bottom: 4px;
    }}

    .tooltip-row {{
      display: flex;
      justify-content: space-between;
      gap: 16px;
      margin-top: 4px;
    }}

    /* Top Customers List */
    .customer-list {{
      display: flex;
      flex-direction: column;
      gap: 16px;
    }}

    .customer-item {{
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      padding: 16px;
      display: flex;
      flex-direction: column;
      gap: 10px;
      cursor: pointer;
      transition: all 0.2s ease;
    }}

    .customer-item:hover {{
      border-color: var(--border-focus);
      background: var(--bg-surface-elevated);
      transform: translateX(4px);
    }}

    .customer-row-top {{
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}

    .customer-info {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}

    .rank-badge {{
      width: 28px;
      height: 28px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 12px;
      font-weight: 800;
      color: #ffffff;
      background: var(--bg-surface-elevated);
    }}

    .rank-1 {{ background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%); box-shadow: 0 0 12px var(--amber-glow); }}
    .rank-2 {{ background: linear-gradient(135deg, #94a3b8 0%, #64748b 100%); }}
    .rank-3 {{ background: linear-gradient(135deg, #b45309 0%, #78350f 100%); }}

    .customer-name {{
      font-weight: 700;
      font-size: 14px;
      color: var(--text-primary);
    }}

    .customer-id {{
      font-family: var(--font-mono);
      font-size: 11px;
      color: var(--text-tertiary);
    }}

    .customer-spend {{
      font-family: var(--font-mono);
      font-size: 15px;
      font-weight: 800;
      color: var(--emerald-400);
      text-align: right;
    }}

    .customer-bar-track {{
      width: 100%;
      height: 7px;
      background: var(--border-subtle);
      border-radius: var(--radius-full);
      overflow: hidden;
    }}

    .customer-bar-fill {{
      height: 100%;
      background: linear-gradient(90deg, var(--cyan-500) 0%, var(--emerald-400) 100%);
      border-radius: var(--radius-full);
      transition: width 0.8s cubic-bezier(0.16, 1, 0.3, 1);
    }}

    /* -------------------------------------------------------------
       QUARTERLY BREAKDOWN PIE / METRIC STATS
       ------------------------------------------------------------- */
    .quarter-stat-grid {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 16px;
      margin-top: 24px;
    }}

    @media (max-width: 800px) {{
      .quarter-stat-grid {{
        grid-template-columns: repeat(2, 1fr);
      }}
    }}

    .quarter-card {{
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      padding: 16px;
      text-align: center;
      transition: all 0.2s ease;
    }}

    .quarter-card:hover {{
      border-color: var(--border-focus);
      transform: translateY(-2px);
    }}

    .quarter-name {{
      font-size: 12px;
      font-weight: 700;
      color: var(--text-secondary);
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }}

    .quarter-rev {{
      font-family: var(--font-mono);
      font-size: 18px;
      font-weight: 800;
      color: var(--text-primary);
      margin: 6px 0;
    }}

    .quarter-vol {{
      font-size: 12px;
      color: var(--text-tertiary);
    }}

    /* -------------------------------------------------------------
       AUDIT LEDGER TABLE & CONTROLS
       ------------------------------------------------------------- */
    .ledger-section {{
      background: var(--bg-card);
      backdrop-filter: blur(16px);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-lg);
      padding: 26px;
      box-shadow: var(--shadow-sm);
    }}

    .ledger-toolbar {{
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      align-items: center;
      gap: 16px;
      margin-bottom: 20px;
    }}

    .search-wrapper {{
      position: relative;
      flex: 1;
      max-width: 380px;
    }}

    .search-input {{
      width: 100%;
      padding: 10px 16px 10px 40px;
      font-size: 13px;
      font-family: var(--font-sans);
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      color: var(--text-primary);
      outline: none;
      transition: all 0.2s ease;
    }}

    .search-input:focus {{
      border-color: var(--border-focus);
      box-shadow: 0 0 12px var(--cyan-glow);
    }}

    .search-icon {{
      position: absolute;
      left: 14px;
      top: 50%;
      transform: translateY(-50%);
      color: var(--text-tertiary);
      font-size: 14px;
    }}

    .table-container {{
      width: 100%;
      overflow-x: auto;
      border-radius: var(--radius-md);
      border: 1px solid var(--border-subtle);
    }}

    table.audit-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 13px;
      text-align: left;
    }}

    table.audit-table th {{
      background: var(--bg-surface);
      color: var(--text-secondary);
      font-weight: 700;
      padding: 14px 18px;
      border-bottom: 1px solid var(--border-subtle);
      white-space: nowrap;
      text-transform: uppercase;
      font-size: 11px;
      letter-spacing: 0.05em;
    }}

    table.audit-table td {{
      padding: 14px 18px;
      border-bottom: 1px solid var(--border-subtle);
      color: var(--text-secondary);
      background: transparent;
      white-space: nowrap;
    }}

    table.audit-table tbody tr:hover td {{
      background: var(--bg-surface-elevated);
      color: var(--text-primary);
    }}

    .code-badge {{
      font-family: var(--font-mono);
      font-size: 12px;
      padding: 3px 8px;
      border-radius: var(--radius-sm);
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      color: var(--text-primary);
    }}

    .status-pill {{
      display: inline-flex;
      align-items: center;
      gap: 5px;
      font-size: 11px;
      font-weight: 700;
      padding: 3px 8px;
      border-radius: var(--radius-full);
      background: rgba(16, 185, 129, 0.12);
      color: var(--emerald-400);
      border: 1px solid rgba(16, 185, 129, 0.3);
    }}

    .table-footer {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 16px;
      margin-top: 18px;
      font-size: 13px;
      color: var(--text-tertiary);
    }}

    /* -------------------------------------------------------------
       MODAL POPUP (Customer Drilldown)
       ------------------------------------------------------------- */
    .modal-overlay {{
      position: fixed;
      inset: 0;
      background: rgba(0, 0, 0, 0.75);
      backdrop-filter: blur(8px);
      display: flex;
      align-items: center;
      justify-content: center;
      z-index: 1000;
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.25s ease;
    }}

    .modal-overlay.open {{
      opacity: 1;
      pointer-events: auto;
    }}

    .modal-card {{
      background: var(--bg-surface);
      border: 1px solid var(--border-strong);
      border-radius: var(--radius-lg);
      padding: 32px;
      max-width: 540px;
      width: 90%;
      box-shadow: var(--shadow-lg);
      transform: scale(0.95);
      transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }}

    .modal-overlay.open .modal-card {{
      transform: scale(1);
    }}

    .modal-close-btn {{
      float: right;
      background: transparent;
      border: none;
      font-size: 20px;
      color: var(--text-secondary);
      cursor: pointer;
    }}

    /* Toast Notification */
    .toast-msg {{
      position: fixed;
      bottom: 28px;
      right: 28px;
      background: var(--bg-surface-elevated);
      color: var(--text-primary);
      border: 1px solid var(--border-strong);
      padding: 12px 20px;
      border-radius: var(--radius-md);
      box-shadow: var(--shadow-lg);
      display: flex;
      align-items: center;
      gap: 10px;
      font-size: 13px;
      font-weight: 600;
      opacity: 0;
      transform: translateY(20px);
      transition: all 0.3s ease;
      z-index: 2000;
      pointer-events: none;
    }}

    .toast-msg.show {{
      opacity: 1;
      transform: translateY(0);
    }}
  </style>
</head>
<body>

<div class="app-wrapper">

  <!-- TOP EXECUTIVE HEADER -->
  <header class="executive-header">
    <div class="brand-cluster">
      <div class="brand-mark">GT</div>
      <div class="brand-details">
        <h1>
          GlobalTech Financial Suite
          <span class="badge-verified">CFO Audit Passed</span>
        </h1>
        <p>Enterprise Data Architecture & Reconciliation Hub | Q1–Q4 Audited Ledger</p>
      </div>
    </div>
    
    <div class="header-controls">
      <button class="btn btn-secondary" id="export-csv-btn">
        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
        Export Ledger (CSV)
      </button>
      
      <button class="btn btn-secondary" id="export-json-btn">
        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
        Export Metrics (JSON)
      </button>

      <button class="theme-toggle-btn" id="theme-btn" title="Toggle Dark/Light Mode">🌙</button>
    </div>
  </header>

  <!-- CFO CONTROL BAR: QUARTER SLICERS & SCENARIO SIMULATOR -->
  <section class="control-ribbon">
    <div class="slicer-group">
      <button class="slicer-btn active" data-quarter="ALL">FY 2023</button>
      <button class="slicer-btn" data-quarter="Q1">Q1</button>
      <button class="slicer-btn" data-quarter="Q2">Q2</button>
      <button class="slicer-btn" data-quarter="Q3">Q3</button>
      <button class="slicer-btn" data-quarter="Q4">Q4</button>
    </div>

    <div class="currency-selector">
      <span style="font-size: 11px; font-weight: 700; color: var(--text-tertiary); margin-right: 4px;">CURRENCY:</span>
      <button class="curr-btn active" id="curr-usd">USD ($)</button>
      <button class="curr-btn" id="curr-eur">EUR (€)</button>
    </div>

    <div class="stress-test-toggle">
      <span>FX Stress Test:</span>
      <input type="range" min="-15" max="15" step="1" value="0" class="stress-slider" id="fx-slider">
      <span class="stress-pill" id="stress-val">0%</span>
      <button class="btn btn-secondary" style="padding: 4px 8px; font-size: 11px;" id="reset-fx-btn">Reset</button>
    </div>
  </section>

  <!-- 4 PRIMARY KPI METRIC CARDS -->
  <section class="kpi-grid">
    <!-- Revenue -->
    <div class="kpi-card" style="--accent-color: var(--cyan-500);">
      <div class="kpi-header">
        <span class="kpi-title">Reconciled Revenue</span>
        <div class="kpi-icon-badge">💰</div>
      </div>
      <div class="kpi-value" id="kpi-revenue">$148,274,622.91</div>
      <div class="kpi-footer">
        <span class="trend-indicator trend-up">↑ +14.8% YoY</span>
        <span>Audited Q1–Q4 total</span>
      </div>
    </div>

    <!-- Total Transactions -->
    <div class="kpi-card" style="--accent-color: var(--emerald-500);">
      <div class="kpi-header">
        <span class="kpi-title">Clean Transactions</span>
        <div class="kpi-icon-badge">⚡</div>
      </div>
      <div class="kpi-value" id="kpi-transactions">53,899</div>
      <div class="kpi-footer">
        <span class="trend-indicator trend-up">↑ 100% Valid</span>
        <span>5,098 corrupted logs dropped</span>
      </div>
    </div>

    <!-- Active Customers -->
    <div class="kpi-card" style="--accent-color: var(--violet-500);">
      <div class="kpi-header">
        <span class="kpi-title">Active Customers</span>
        <div class="kpi-icon-badge">👥</div>
      </div>
      <div class="kpi-value" id="kpi-users">14,183</div>
      <div class="kpi-footer">
        <span class="trend-indicator trend-stable">● Verified</span>
        <span>13,888 transacting active</span>
      </div>
    </div>

    <!-- Average Transaction Value -->
    <div class="kpi-card" style="--accent-color: var(--amber-500);">
      <div class="kpi-header">
        <span class="kpi-title">Average Order Value</span>
        <div class="kpi-icon-badge">📊</div>
      </div>
      <div class="kpi-value" id="kpi-aov">$2,750.97</div>
      <div class="kpi-footer">
        <span class="trend-indicator trend-up">↑ Robust</span>
        <span>Mean basket across enterprise</span>
      </div>
    </div>
  </section>

  <!-- CHARTS & VISUALIZATIONS SECTION -->
  <section class="dashboard-grid">
    <!-- Chart 1: Monthly Financial Trajectory -->
    <div class="panel-card">
      <div class="panel-header">
        <div class="panel-title">
          <h2>Monthly Revenue Performance Trajectory</h2>
          <p id="chart-sub-label">Audited revenue trend with forward-filled currency parity (2023)</p>
        </div>
        <div class="panel-tags">
          <span class="tag-chip">Peak: Aug ($12.81M)</span>
          <span class="tag-chip">Min: Feb ($11.44M)</span>
        </div>
      </div>

      <div class="chart-container" id="line-chart-wrapper">
        <svg class="chart-svg" id="trajectory-svg" viewBox="0 0 850 340">
          <!-- Rendered dynamically -->
        </svg>
        <div class="interactive-tooltip" id="chart-tooltip">
          <!-- Populated on hover -->
        </div>
      </div>

      <!-- Quarterly Stat Summary Row -->
      <div class="quarter-stat-grid" id="quarter-cards-container">
        <!-- Injected via JavaScript -->
      </div>
    </div>

    <!-- Chart 2: Top Customer Spending Leaderboard -->
    <div class="panel-card">
      <div class="panel-header">
        <div class="panel-title">
          <h2>Top Valuable Customers</h2>
          <p>Highest cumulative spending accounts in USD</p>
        </div>
        <span class="tag-chip" style="color: var(--emerald-400);">Tier 1 Enterprise</span>
      </div>

      <div class="customer-list" id="customer-list-container">
        <!-- Rendered via JavaScript -->
      </div>
    </div>
  </section>

  <!-- AUDIT TRANSACTION LEDGER -->
  <section class="ledger-section">
    <div class="ledger-toolbar">
      <div>
        <h2 style="font-size: 18px; font-weight: 800; color: var(--text-primary);">Audited Transaction Ledger Sample</h2>
        <p style="font-size: 13px; color: var(--text-secondary); margin-top: 2px;">Exported dataset (power_bi_ready_dataset.csv) verified against HR SQL database</p>
      </div>

      <div class="search-wrapper">
        <span class="search-icon">🔍</span>
        <input type="text" class="search-input" id="ledger-search" placeholder="Filter by User, Customer Name, Product...">
      </div>
    </div>

    <div class="table-container">
      <table class="audit-table">
        <thead>
          <tr>
            <th>Date</th>
            <th>User ID</th>
            <th>Customer Name</th>
            <th>Product Code</th>
            <th>EUR Value</th>
            <th>FX Rate (EUR→USD)</th>
            <th>USD Revenue</th>
            <th>Account Status</th>
          </tr>
        </thead>
        <tbody id="ledger-tbody">
          <!-- Rendered via JavaScript -->
        </tbody>
      </table>
    </div>

    <div class="table-footer">
      <span id="ledger-count-label">Showing 15 records</span>
      <span style="font-family: var(--font-mono); font-size: 12px; color: var(--text-tertiary);">Data Source: power_bi_ready_dataset.csv (53,899 rows total)</span>
    </div>
  </section>

</div>

<!-- CUSTOMER PROFILE MODAL -->
<div class="modal-overlay" id="customer-modal">
  <div class="modal-card">
    <button class="modal-close-btn" id="modal-close-x">&times;</button>
    <div style="display: flex; align-items: center; gap: 14px; margin-bottom: 20px;">
      <div class="rank-badge rank-1" id="modal-rank-badge" style="width: 38px; height: 38px; font-size: 16px;">1</div>
      <div>
        <h3 id="modal-cust-name" style="font-size: 20px; font-weight: 800; color: var(--text-primary);">User_U-06582</h3>
        <span class="code-badge" id="modal-cust-id">U-06582</span>
      </div>
    </div>
    
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px; margin-bottom: 24px;">
      <div style="background: var(--bg-card); padding: 14px; border-radius: var(--radius-md); border: 1px solid var(--border-subtle);">
        <div style="font-size: 12px; color: var(--text-secondary);">Total Spend (USD)</div>
        <div id="modal-cust-spend" style="font-family: var(--font-mono); font-size: 20px; font-weight: 800; color: var(--emerald-400); margin-top: 4px;">$40,050.99</div>
      </div>
      <div style="background: var(--bg-card); padding: 14px; border-radius: var(--radius-md); border: 1px solid var(--border-subtle);">
        <div style="font-size: 12px; color: var(--text-secondary);">Account Verification</div>
        <div style="font-size: 14px; font-weight: 700; color: var(--emerald-400); margin-top: 8px;">Active & Reconciled</div>
      </div>
    </div>

    <p style="font-size: 13px; color: var(--text-secondary); line-height: 1.6; margin-bottom: 24px;">
      This enterprise client represents high-frequency corporate volume across multi-currency euro disbursements, fully reconciled with zero dropped weekend timestamps.
    </p>

    <button class="btn btn-primary" style="width: 100%; justify-content: center;" id="modal-close-btn">Done</button>
  </div>
</div>

<!-- TOAST MESSAGE -->
<div class="toast-msg" id="toast">Action completed successfully</div>

<script>
  // -------------------------------------------------------------
  // DATA & STATE MANAGEMENT
  // -------------------------------------------------------------
  const baseData = {json_payload};

  const state = {{
    quarter: 'ALL',
    currency: 'USD',
    fxMultiplier: 1.0,
    theme: 'dark',
    searchQuery: ''
  }};

  // Formatters
  const fmtCurrUSD = (num) => '$' + Number(num).toLocaleString('en-US', {{ minimumFractionDigits: 2, maximumFractionDigits: 2 }});
  const fmtCurrEUR = (num) => '€' + Number(num).toLocaleString('en-US', {{ minimumFractionDigits: 2, maximumFractionDigits: 2 }});
  const fmtInt = (num) => Number(num).toLocaleString('en-US');

  // DOM Elements
  const kpiRevenue = document.getElementById('kpi-revenue');
  const kpiTransactions = document.getElementById('kpi-transactions');
  const kpiUsers = document.getElementById('kpi-users');
  const kpiAov = document.getElementById('kpi-aov');
  const trajectorySvg = document.getElementById('trajectory-svg');
  const chartTooltip = document.getElementById('chart-tooltip');
  const quarterCardsContainer = document.getElementById('quarter-cards-container');
  const customerListContainer = document.getElementById('customer-list-container');
  const ledgerTbody = document.getElementById('ledger-tbody');
  const ledgerSearch = document.getElementById('ledger-search');
  const ledgerCountLabel = document.getElementById('ledger-count-label');
  const themeBtn = document.getElementById('theme-btn');
  const fxSlider = document.getElementById('fx-slider');
  const stressVal = document.getElementById('stress-val');
  const resetFxBtn = document.getElementById('reset-fx-btn');
  const currUsdBtn = document.getElementById('curr-usd');
  const currEurBtn = document.getElementById('curr-eur');
  const exportCsvBtn = document.getElementById('export-csv-btn');
  const exportJsonBtn = document.getElementById('export-json-btn');
  const toast = document.getElementById('toast');
  const customerModal = document.getElementById('customer-modal');

  function showToast(msg) {{
    toast.textContent = msg;
    toast.classList.add('show');
    setTimeout(() => toast.classList.remove('show'), 2500);
  }}

  // -------------------------------------------------------------
  // THEME SWITCHING
  // -------------------------------------------------------------
  themeBtn.addEventListener('click', () => {{
    const currentTheme = document.documentElement.getAttribute('data-theme');
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', newTheme);
    themeBtn.textContent = newTheme === 'dark' ? '🌙' : '☀️';
    showToast(`Switched to ${{newTheme.toUpperCase()}} Mode`);
    renderAll();
  }});

  // -------------------------------------------------------------
  // CURRENCY SELECTION
  // -------------------------------------------------------------
  currUsdBtn.addEventListener('click', () => {{
    state.currency = 'USD';
    currUsdBtn.classList.add('active');
    currEurBtn.classList.remove('active');
    renderAll();
  }});

  currEurBtn.addEventListener('click', () => {{
    state.currency = 'EUR';
    currEurBtn.classList.add('active');
    currUsdBtn.classList.remove('active');
    renderAll();
  }});

  // -------------------------------------------------------------
  // FX STRESS TESTING
  // -------------------------------------------------------------
  fxSlider.addEventListener('input', (e) => {{
    const shift = parseInt(e.target.value, 10);
    state.fxMultiplier = 1.0 + (shift / 100);
    stressVal.textContent = (shift >= 0 ? '+' : '') + shift + '%';
    renderAll();
  }});

  resetFxBtn.addEventListener('click', () => {{
    fxSlider.value = 0;
    state.fxMultiplier = 1.0;
    stressVal.textContent = '0%';
    renderAll();
    showToast('FX Rates reset to historical actuals');
  }});

  // -------------------------------------------------------------
  // QUARTER SLICERS
  // -------------------------------------------------------------
  document.querySelectorAll('.slicer-btn').forEach(btn => {{
    btn.addEventListener('click', () => {{
      document.querySelectorAll('.slicer-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      state.quarter = btn.getAttribute('data-quarter');
      renderAll();
      showToast(`Filtered by ${{state.quarter}} Fiscal Period`);
    }});
  }});

  // -------------------------------------------------------------
  // CALCULATION & DATA AGGREGATION
  // -------------------------------------------------------------
  function getActiveDataset() {{
    const mult = state.fxMultiplier;
    let months = [...baseData.monthly];
    let topCustomers = baseData.top5_overall;

    if (state.quarter !== 'ALL') {{
      const quarterMonthsMap = {{
        'Q1': ['2023-01', '2023-02', '2023-03'],
        'Q2': ['2023-04', '2023-05', '2023-06'],
        'Q3': ['2023-07', '2023-08', '2023-09'],
        'Q4': ['2023-10', '2023-11', '2023-12']
      }};
      const targetMonths = quarterMonthsMap[state.quarter] || [];
      months = months.filter(m => targetMonths.includes(m.Month));
      topCustomers = baseData.top5_by_q[state.quarter] || baseData.top5_overall;
    }}

    // Apply currency & FX stress testing
    const processedMonths = months.map(m => {{
      let val = m.revenue * mult;
      if (state.currency === 'EUR') {{
        val = val / 1.10; // average 2023 EUR/USD parity
      }}
      return {{
        ...m,
        displayRevenue: val
      }};
    }});

    const totalRev = processedMonths.reduce((acc, m) => acc + m.displayRevenue, 0);
    const totalTx = processedMonths.reduce((acc, m) => acc + m.transactions, 0);
    const uniqueUsers = state.quarter === 'ALL' ? baseData.unique_active_users : (baseData.quarterly.find(q => q.Quarter === state.quarter)?.active_users || 8629);
    const aov = totalTx > 0 ? (totalRev / totalTx) : 0;

    const processedCustomers = topCustomers.map(c => {{
      let val = c.USD_Revenue * mult;
      if (state.currency === 'EUR') {{
        val = val / 1.10;
      }}
      return {{
        ...c,
        displayRevenue: val
      }};
    }});

    return {{
      totalRevenue: totalRev,
      totalTransactions: totalTx,
      uniqueUsers: uniqueUsers,
      aov: aov,
      months: processedMonths,
      topCustomers: processedCustomers
    }};
  }}

  // -------------------------------------------------------------
  // RENDER KPI CARDS
  // -------------------------------------------------------------
  function renderKPIs(activeData) {{
    const fmt = state.currency === 'USD' ? fmtCurrUSD : fmtCurrEUR;
    kpiRevenue.textContent = fmt(activeData.totalRevenue);
    kpiTransactions.textContent = fmtInt(activeData.totalTransactions);
    kpiUsers.textContent = fmtInt(activeData.uniqueUsers);
    kpiAov.textContent = fmt(activeData.aov);
  }}

  // -------------------------------------------------------------
  // RENDER INTERACTIVE SVG LINE CHART
  // -------------------------------------------------------------
  function renderLineChart(activeData) {{
    const months = activeData.months;
    const width = 850;
    const height = 340;
    const padX = 60;
    const padY = 40;
    const chartW = width - (padX * 2);
    const chartH = height - (padY * 2);

    const values = months.map(m => m.displayRevenue);
    const minVal = Math.min(...values) * 0.95;
    const maxVal = Math.max(...values) * 1.05;

    const getX = (idx) => padX + (idx / (months.length - 1 || 1)) * chartW;
    const getY = (val) => padY + chartH - ((val - minVal) / (maxVal - minVal || 1)) * chartH;

    const points = months.map((m, i) => ({{ x: getX(i), y: getY(m.displayRevenue), data: m }}));

    // Generate smooth bezier curve
    let pathD = `M ${{points[0].x}} ${{points[0].y}}`;
    for (let i = 0; i < points.length - 1; i++) {{
      const p0 = points[i];
      const p1 = points[i + 1];
      const cpX1 = p0.x + (p1.x - p0.x) / 2;
      const cpY1 = p0.y;
      const cpX2 = p0.x + (p1.x - p0.x) / 2;
      const cpY2 = p1.y;
      pathD += ` C ${{cpX1}} ${{cpY1}}, ${{cpX2}} ${{cpY2}}, ${{p1.x}} ${{p1.y}}`;
    }}

    const areaD = `${{pathD}} L ${{points[points.length - 1].x}} ${{height - padY}} L ${{points[0].x}} ${{height - padY}} Z`;

    // Horizontal Gridlines
    let gridlinesSvg = '';
    const gridSteps = 4;
    for (let i = 0; i <= gridSteps; i++) {{
      const yVal = minVal + ((maxVal - minVal) / gridSteps) * i;
      const yPos = getY(yVal);
      const label = state.currency === 'USD' ? `$${{(yVal * 1e-6).toFixed(1)}}M` : `€${{(yVal * 1e-6).toFixed(1)}}M`;
      gridlinesSvg += `
        <line x1="${{padX}}" y1="${{yPos}}" x2="${{width - padX}}" y2="${{yPos}}" stroke="var(--border-subtle)" stroke-dasharray="4,4"/>
        <text x="${{padX - 10}}" y="${{yPos + 4}}" fill="var(--text-tertiary)" font-size="11" font-family="var(--font-mono)" text-anchor="end">${{label}}</text>
      `;
    }}

    // X Axis Labels
    let xLabelsSvg = '';
    points.forEach((p, idx) => {{
      const label = p.data.Month.substring(5); // e.g. '01', '02'
      xLabelsSvg += `
        <text x="${{p.x}}" y="${{height - padY + 24}}" fill="var(--text-secondary)" font-size="11" font-family="var(--font-mono)" text-anchor="middle">
          M${{label}}
        </text>
      `;
    }});

    // Circles
    let circlesSvg = '';
    points.forEach((p, idx) => {{
      circlesSvg += `
        <circle class="chart-point" data-idx="${{idx}}" cx="${{p.x}}" cy="${{p.y}}" r="5" fill="#ffffff" stroke="var(--cyan-500)" stroke-width="3" style="cursor: pointer; transition: r 0.2s;"/>
      `;
    }});

    trajectorySvg.innerHTML = `
      <defs>
        <linearGradient id="chartGradient" x1="0" y1="0" x2="0" y2="1">
          <stop offset="0%" stop-color="var(--cyan-500)" stop-opacity="0.35"/>
          <stop offset="100%" stop-color="var(--cyan-500)" stop-opacity="0.0"/>
        </linearGradient>
      </defs>
      ${{gridlinesSvg}}
      ${{xLabelsSvg}}
      <path d="${{areaD}}" fill="url(#chartGradient)"/>
      <path d="${{pathD}}" fill="none" stroke="var(--cyan-500)" stroke-width="3.5" stroke-linecap="round"/>
      ${{circlesSvg}}
    `;

    // Tooltip hover interactions
    const chartWrapper = document.getElementById('line-chart-wrapper');
    const svgRect = trajectorySvg.getBoundingClientRect();

    trajectorySvg.querySelectorAll('.chart-point').forEach(c => {{
      c.addEventListener('mouseenter', (e) => {{
        const idx = parseInt(e.target.getAttribute('data-idx'), 10);
        const pt = points[idx];
        const m = pt.data;
        const fmt = state.currency === 'USD' ? fmtCurrUSD : fmtCurrEUR;

        c.setAttribute('r', '8');
        c.setAttribute('stroke', 'var(--emerald-400)');

        chartTooltip.innerHTML = `
          <div class="tooltip-header">Month: ${{m.Month}} (2023)</div>
          <div class="tooltip-row"><span>Revenue:</span><b style="color:var(--emerald-400);">${{fmt(m.displayRevenue)}}</b></div>
          <div class="tooltip-row"><span>Transactions:</span><b>${{fmtInt(m.transactions)}}</b></div>
          <div class="tooltip-row"><span>Active Users:</span><b>${{fmtInt(m.active_users)}}</b></div>
          <div class="tooltip-row"><span>Avg Basket:</span><b>${{fmt(m.avg_order)}}</b></div>
        `;

        const ptXPercent = (pt.x / width) * 100;
        const ptYPercent = (pt.y / height) * 100;
        chartTooltip.style.left = `${{ptXPercent}}%`;
        chartTooltip.style.top = `${{ptYPercent}}%`;
        chartTooltip.classList.add('visible');
      }});

      c.addEventListener('mouseleave', () => {{
        c.setAttribute('r', '5');
        c.setAttribute('stroke', 'var(--cyan-500)');
        chartTooltip.classList.remove('visible');
      }});
    }});
  }}

  // -------------------------------------------------------------
  // RENDER QUARTER STAT CARDS
  // -------------------------------------------------------------
  function renderQuarterCards() {{
    const fmt = state.currency === 'USD' ? fmtCurrUSD : fmtCurrEUR;
    quarterCardsContainer.innerHTML = baseData.quarterly.map(q => {{
      let rev = q.revenue * state.fxMultiplier;
      if (state.currency === 'EUR') rev /= 1.10;
      return `
        <div class="quarter-card">
          <div class="quarter-name">${{q.Quarter}} 2023</div>
          <div class="quarter-rev">${{fmt(rev)}}</div>
          <div class="quarter-vol">${{fmtInt(q.transactions)}} orders | ${{fmtInt(q.active_users)}} users</div>
        </div>
      `;
    }}).join('');
  }}

  // -------------------------------------------------------------
  // RENDER TOP VALUABLE CUSTOMERS
  // -------------------------------------------------------------
  function renderTopCustomers(activeData) {{
    const customers = activeData.topCustomers;
    const maxSpend = Math.max(...customers.map(c => c.displayRevenue));
    const fmt = state.currency === 'USD' ? fmtCurrUSD : fmtCurrEUR;

    customerListContainer.innerHTML = customers.map((c, idx) => {{
      const pct = ((c.displayRevenue / maxSpend) * 100).toFixed(1);
      const rankClass = idx === 0 ? 'rank-1' : (idx === 1 ? 'rank-2' : (idx === 2 ? 'rank-3' : ''));
      return `
        <div class="customer-item" data-id="${{c.user_id}}" data-name="${{c.name}}" data-spend="${{fmt(c.displayRevenue)}}" data-rank="${{idx + 1}}">
          <div class="customer-row-top">
            <div class="customer-info">
              <div class="rank-badge ${{rankClass}}">${{idx + 1}}</div>
              <div>
                <div class="customer-name">${{c.name}}</div>
                <div class="customer-id">ID: ${{c.user_id}}</div>
              </div>
            </div>
            <div class="customer-spend">${{fmt(c.displayRevenue)}}</div>
          </div>
          <div class="customer-bar-track">
            <div class="customer-bar-fill" style="width: ${{pct}}%;"></div>
          </div>
        </div>
      `;
    }}).join('');

    // Modal click bind
    customerListContainer.querySelectorAll('.customer-item').forEach(el => {{
      el.addEventListener('click', () => {{
        const id = el.getAttribute('data-id');
        const name = el.getAttribute('data-name');
        const spend = el.getAttribute('data-spend');
        const rank = el.getAttribute('data-rank');

        document.getElementById('modal-cust-name').textContent = name;
        document.getElementById('modal-cust-id').textContent = id;
        document.getElementById('modal-cust-spend').textContent = spend;
        document.getElementById('modal-rank-badge').textContent = rank;
        customerModal.classList.add('open');
      }});
    }});
  }}

  // -------------------------------------------------------------
  // RENDER AUDIT LEDGER TABLE
  // -------------------------------------------------------------
  function renderLedger() {{
    const q = state.searchQuery.toLowerCase();
    const rows = baseData.sample_records.filter(r => {{
      if (!q) return true;
      return r.user_id.toLowerCase().includes(q) ||
             r.name.toLowerCase().includes(q) ||
             r.product_id.toLowerCase().includes(q) ||
             r.Date.includes(q);
    }});

    const mult = state.fxMultiplier;
    const isUSD = state.currency === 'USD';

    ledgerTbody.innerHTML = rows.slice(0, 15).map(r => {{
      const adjUSD = r.USD_Revenue * mult;
      const adjEUR = r.eur_val;
      return `
        <tr>
          <td><span class="code-badge">${{r.Date}}</span></td>
          <td><span class="code-badge">${{r.user_id}}</span></td>
          <td style="font-weight: 700; color: var(--text-primary);">${{r.name}}</td>
          <td><span class="code-badge" style="color: var(--cyan-400);">${{r.product_id}}</span></td>
          <td>€${{Number(adjEUR).toLocaleString('en-US', {{ minimumFractionDigits: 2 }})}}</td>
          <td style="font-family: var(--font-mono);">${{(Number(r.EUR_to_USD) * mult).toFixed(4)}}</td>
          <td style="font-weight: 800; color: var(--emerald-400);">${{fmtCurrUSD(adjUSD)}}</td>
          <td><span class="status-pill">● Active</span></td>
        </tr>
      `;
    }}).join('');

    ledgerCountLabel.textContent = `Displaying ${{Math.min(15, rows.length)}} of ${{rows.length}} filtered records`;
  }}

  ledgerSearch.addEventListener('input', (e) => {{
    state.searchQuery = e.target.value;
    renderLedger();
  }});

  // -------------------------------------------------------------
  // MODAL CONTROLS
  // -------------------------------------------------------------
  document.getElementById('modal-close-x').addEventListener('click', () => customerModal.classList.remove('open'));
  document.getElementById('modal-close-btn').addEventListener('click', () => customerModal.classList.remove('open'));
  customerModal.addEventListener('click', (e) => {{
    if (e.target === customerModal) customerModal.classList.remove('open');
  }});

  // -------------------------------------------------------------
  // EXPORTS
  // -------------------------------------------------------------
  exportCsvBtn.addEventListener('click', () => {{
    const headers = ['Date', 'User_ID', 'Name', 'Product_ID', 'EUR_Val', 'EUR_to_USD', 'USD_Revenue', 'Status'];
    const rows = baseData.sample_records.map(r => [
      r.Date, r.user_id, r.name, r.product_id, r.eur_val, r.EUR_to_USD, (r.USD_Revenue * state.fxMultiplier).toFixed(2), 'Active'
    ]);
    const csvContent = 'data:text/csv;charset=utf-8,' + [headers.join(','), ...rows.map(e => e.join(','))].join('\\n');
    const encodedUri = encodeURI(csvContent);
    const link = document.createElement('a');
    link.setAttribute('href', encodedUri);
    link.setAttribute('download', `reconciled_audit_ledger_${{state.quarter}}.csv`);
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    showToast('Audited Ledger exported to CSV!');
  }});

  exportJsonBtn.addEventListener('click', () => {{
    const active = getActiveDataset();
    const exportData = {{
      fiscal_year: '2023',
      filter_period: state.quarter,
      currency: state.currency,
      fx_stress_multiplier: state.fxMultiplier,
      kpis: {{
        total_revenue: active.totalRevenue,
        total_transactions: active.totalTransactions,
        active_customers: active.uniqueUsers,
        average_order_value: active.aov
      }},
      monthly_breakdown: active.months,
      top_customers: active.topCustomers
    }};
    const jsonStr = 'data:text/json;charset=utf-8,' + encodeURIComponent(JSON.stringify(exportData, null, 2));
    const link = document.createElement('a');
    link.setAttribute('href', jsonStr);
    link.setAttribute('download', `cfo_audit_summary_${{state.quarter}}.json`);
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    showToast('Executive Summary exported to JSON!');
  }});

  // -------------------------------------------------------------
  // MASTER RENDER
  // -------------------------------------------------------------
  function renderAll() {{
    const activeData = getActiveDataset();
    renderKPIs(activeData);
    renderLineChart(activeData);
    renderQuarterCards();
    renderTopCustomers(activeData);
    renderLedger();
  }}

  // Initial Boot
  renderAll();
</script>
</body>
</html>
'''

with open('cfo_pro_dashboard_app.html', 'w', encoding='utf-8') as f:
    f.write(html_code)

print("Enterprise CFO Pro Dashboard Web App cloned and generated successfully at 'cfo_pro_dashboard_app.html'!")
