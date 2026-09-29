<template>
  <div class="app">

    <!-- =========================
         NAVBAR
         ========================= -->

    <nav class="navbar">

      <div class="nav-container">

        <!-- Logo -->
        <router-link to="/" class="logo">
          T&C Lens
        </router-link>


        <!-- Desktop Navigation -->
        <div class="nav-links">

          <router-link to="/" class="nav-link">
            Home
          </router-link>

          <router-link to="/analyze" class="nav-link">
            Analyze
          </router-link>

          <router-link to="/history" class="nav-link">
            History
          </router-link>

          <router-link to="/about" class="nav-link">
            About
          </router-link>

        </div>


        <!-- Desktop Authentication -->
        <div class="nav-auth">

          <button class="auth-login">
            Log in
          </button>

          <button class="auth-signup">
            Sign up
          </button>

        </div>


        <!-- Mobile Hamburger -->
        <button
          class="hamburger"
          :class="{ active: menuOpen }"
          @click="menuOpen = !menuOpen"
          aria-label="Toggle navigation"
        >

          <span></span>
          <span></span>
          <span></span>

        </button>

      </div>


      <!-- =========================
           MOBILE MENU
           ========================= -->

      <div
        v-if="menuOpen"
        class="mobile-menu"
      >

        <div class="mobile-links">

          <router-link
            to="/"
            class="mobile-link"
            @click="closeMenu"
          >
            Home
          </router-link>

          <router-link
            to="/analyze"
            class="mobile-link"
            @click="closeMenu"
          >
            Analyze
          </router-link>

          <router-link
            to="/history"
            class="mobile-link"
            @click="closeMenu"
          >
            History
          </router-link>

          <router-link
            to="/about"
            class="mobile-link"
            @click="closeMenu"
          >
            About
          </router-link>

        </div>


        <!-- Separator -->
        <div class="mobile-divider"></div>


        <!-- Mobile Authentication -->
        <div class="mobile-auth">

          <button class="mobile-login">
            Log in
          </button>

          <button class="mobile-signup">
            Sign up
          </button>

        </div>

      </div>

    </nav>


    <!-- =========================
         PAGE
         ========================= -->

    <main>
      <router-view />
    </main>

  </div>
</template>


<script setup>
import { ref } from 'vue'

const menuOpen = ref(false)

const closeMenu = () => {
  menuOpen.value = false
}
</script>


<style>
/* =========================
   GENERAL
   ========================= */

* {
  box-sizing: border-box;
}

html {
  scroll-behavior: smooth;
}

body {
  margin: 0;

  font-family:
    'Segoe UI',
    Tahoma,
    Geneva,
    Verdana,
    sans-serif;

  background: #f8f9fa;
  color: #333;
}

.app {
  min-height: 100vh;
}


/* =========================
   NAVBAR
   ========================= */

.navbar {
  position: fixed;

  top: 0;
  left: 0;

  width: 100%;

  background: rgba(255, 255, 255, 0.96);

  border-bottom: 1px solid #e5e7eb;

  z-index: 100;

  backdrop-filter: blur(10px);
}


/* =========================
   NAV CONTAINER
   ========================= */

.nav-container {
  width: 100%;

  /*
    1100px content + 40px left/right padding
    = 1180px total

    This matches the Home section layout.
  */
  max-width: 1180px;

  margin: 0 auto;

  padding: 16px 40px;

  display: flex;

  align-items: center;

  position: relative;
}


/* =========================
   LOGO
   ========================= */

.logo {
  text-decoration: none;

  color: #2c3e50;

  font-size: 20px;
  font-weight: 700;

  white-space: nowrap;

  transition: color 0.2s ease;
}

.logo:hover {
  color: #42b883;
}


/* =========================
   DESKTOP NAVIGATION
   ========================= */

.nav-links {
  position: absolute;

  left: 50%;

  transform: translateX(-50%);

  display: flex;

  align-items: center;

  gap: 4px;
}

.nav-link {
  text-decoration: none;

  color: #667085;

  padding: 8px 14px;

  border-radius: 6px;

  font-size: 15px;
  font-weight: 500;

  transition:
    color 0.2s ease,
    background 0.2s ease;
}

.nav-link:hover {
  color: #2c3e50;

  background: #f1f3f5;
}

.nav-link.router-link-active {
  background: #42b883;

  color: white;
}


/* =========================
   AUTHENTICATION
   ========================= */

.nav-auth {
  margin-left: auto;

  display: flex;

  align-items: center;

  gap: 8px;
}

.auth-login,
.auth-signup {
  border: none;

  font-family: inherit;

  font-size: 14px;
  font-weight: 600;

  padding: 8px 14px;

  border-radius: 6px;

  cursor: pointer;

  transition:
    background 0.2s ease,
    color 0.2s ease;
}


/* Login */

.auth-login {
  background: transparent;

  color: #555;
}

.auth-login:hover {
  background: #f1f3f5;

  color: #2c3e50;
}


/* Sign up */

.auth-signup {
  background: #42b883;

  color: white;
}

.auth-signup:hover {
  background: #369f6e;
}


/* =========================
   HAMBURGER
   ========================= */

.hamburger {
  display: none;

  margin-left: auto;

  width: 42px;
  height: 42px;

  padding: 9px;

  background: transparent;

  border: none;

  border-radius: 6px;

  cursor: pointer;

  flex-direction: column;

  justify-content: center;

  gap: 5px;
}

.hamburger:hover {
  background: #f1f3f5;
}

.hamburger span {
  display: block;

  width: 22px;
  height: 2px;

  margin: 0 auto;

  background: #2c3e50;

  border-radius: 2px;

  transition:
    transform 0.25s ease,
    opacity 0.25s ease;
}


/* Hamburger → X */

.hamburger.active span:nth-child(1) {
  transform: translateY(7px) rotate(45deg);
}

.hamburger.active span:nth-child(2) {
  opacity: 0;
}

.hamburger.active span:nth-child(3) {
  transform: translateY(-7px) rotate(-45deg);
}


/* =========================
   MOBILE MENU
   ========================= */

.mobile-menu {
  display: none;
}


/* =========================
   MOBILE
   ========================= */

@media (max-width: 800px) {

  .nav-container {
    padding: 14px 25px;
  }


  /* Hide desktop */

  .nav-links,
  .nav-auth {
    display: none;
  }


  /* Show hamburger */

  .hamburger {
    display: flex;
  }


  /* Mobile dropdown */

  .mobile-menu {
    display: block;

    width: 100%;

    padding: 10px 25px 24px;

    background: white;

    border-top: 1px solid #f0f1f2;
  }


  /* Links */

  .mobile-links {
    display: flex;

    flex-direction: column;

    align-items: stretch;
  }

  .mobile-link {
    display: block;

    padding: 13px 5px;

    text-decoration: none;

    color: #555;

    font-size: 16px;
    font-weight: 500;

    border-radius: 6px;

    transition:
      color 0.2s ease,
      background 0.2s ease;
  }

  .mobile-link:hover {
    background: #f1f3f5;

    color: #2c3e50;
  }

  .mobile-link.router-link-active {
    color: #42b883;

    font-weight: 600;
  }


  /* Divider */

  .mobile-divider {
    height: 1px;

    margin: 12px 5px 16px;

    background: #e5e7eb;
  }


  /* Authentication */

  .mobile-auth {
    display: flex;

    flex-direction: column;

    gap: 8px;
  }

  .mobile-login,
  .mobile-signup {
    width: 100%;

    padding: 11px 14px;

    border-radius: 6px;

    font-family: inherit;

    font-size: 15px;
    font-weight: 600;

    cursor: pointer;
  }


  .mobile-login {
    background: white;

    color: #555;

    border: 1px solid #d0d5dd;
  }

  .mobile-login:hover {
    background: #f8f9fa;
  }


  .mobile-signup {
    background: #42b883;

    color: white;

    border: 1px solid #42b883;
  }

  .mobile-signup:hover {
    background: #369f6e;
  }
}


/* =========================
   SMALL MOBILE
   ========================= */

@media (max-width: 600px) {

  .nav-container {
    padding: 13px 20px;
  }

  .mobile-menu {
    padding-left: 20px;
    padding-right: 20px;
  }

  .logo {
    font-size: 19px;
  }
}
</style>