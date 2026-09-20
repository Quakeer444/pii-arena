"use client";

import { Moon, Sun } from "lucide-react";
import { useTheme } from "next-themes";

export function ThemeToggle() {
  const { setTheme } = useTheme();

  return (
    <button
      type="button"
      className="icon-button theme-toggle"
      title="Switch color theme"
      onClick={() => setTheme(theme => theme === "light" ? "dark" : "light")}
    >
      <span className="theme-to-light">
        <Sun size={16} aria-hidden="true" />
        <span className="sr-only">Switch to light theme</span>
      </span>
      <span className="theme-to-dark">
        <Moon size={16} aria-hidden="true" />
        <span className="sr-only">Switch to dark theme</span>
      </span>
    </button>
  );
}
