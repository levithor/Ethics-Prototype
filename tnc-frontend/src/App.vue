<template>
  <div class="app">
    <nav class="navbar">
      <div class="nav-container">
        <router-link to="/" class="logo">
          T&C Summarizer
        </router-link>

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
      </div>
    </nav>

    <main>
      <router-view />
    </main>
  </div>
</template>

<style>
* {
  box-sizing: border-box;
}

body {
  margin: 0;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  background: #f8f9fa;
  color: #333;
}

.app {
  min-height: 100vh;
}

.navbar {
  background: white;
  border-bottom: 1px solid #e5e7eb;
  position: sticky;
  top: 0;
  z-index: 100;
}

.nav-container {
  max-width: 1100px;
  margin: 0 auto;
  padding: 16px 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.logo {
  text-decoration: none;
  color: #2c3e50;
  font-size: 20px;
  font-weight: 700;
}

.nav-links {
  display: flex;
  gap: 8px;
}

.nav-link {
  text-decoration: none;
  color: #555;
  padding: 8px 14px;
  border-radius: 6px;
  font-weight: 500;
  transition: 0.2s;
}

.nav-link:hover {
  background: #f1f3f5;
}

.nav-link.router-link-active {
  background: #42b883;
  color: white;
}

@media (max-width: 600px) {
  .nav-container {
    flex-direction: column;
    gap: 12px;
  }

  .nav-links {
    width: 100%;
    justify-content: center;
    flex-wrap: wrap;
  }
}
</style>