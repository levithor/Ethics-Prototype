<template>
  <div class="home">

    <!-- =========================
         HERO
         ========================= -->

    <section class="hero">
      <div class="hero-content">
        <h1>Understand what you're agreeing to.</h1>

        <p>
          Turn complicated Terms & Conditions and Privacy Policies into clear,
          understandable information before you accept.
        </p>

        <div class="hero-buttons">
          <router-link to="/analyze" class="btn-primary">
            Analyze a document
          </router-link>

          <router-link to="/about" class="btn-secondary">
            Learn more
          </router-link>
        </div>
      </div>
    </section>


    <!-- =========================
         WHAT YOU CAN ANALYZE
         ========================= -->

    <section class="document-section">

      <div class="document-content">

        <!-- Left -->
        <div class="document-heading">

          <div class="document-eyebrow">
            WHAT YOU CAN ANALYZE
          </div>

          <h2>
            What can you analyze?
          </h2>

          <p>
            From everyday online agreements to policies you accept without
            reading, T&C Lens helps you make sense of the fine print.
          </p>

        </div>


        <!-- Right -->
        <div class="document-pile">

          <div
            v-for="(document, index) in documentTypes"
            :key="document"
            class="document-paper"
            :class="`document-paper-${index + 1}`"
          >
            <div class="paper-fold"></div>

            <div class="paper-content">

              <div class="paper-lines">
                <span></span>
                <span></span>
                <span></span>
              </div>

              <div class="paper-title">
                {{ document }}
              </div>

              <div class="paper-lines short">
                <span></span>
                <span></span>
              </div>

            </div>

          </div>

        </div>

      </div>

    </section>


    <!-- =========================
         HOW WE WILL HELP
         ========================= -->

    <section class="analyze-section">

      <div class="analyze-wrapper">

        <div class="section-heading">
          <h2>How we will help</h2>
        </div>


        <div class="analyze-content">

          <!-- Left -->
          <div class="feature-navigation">

            <div class="feature-list">

              <button
                v-for="(feature, index) in features"
                :key="feature.number"
                class="feature-tab"
                :class="{ active: activeFeature === index }"
                @mouseenter="activeFeature = index"
                @focus="activeFeature = index"
                @click="activeFeature = index"
              >

                <span class="feature-number">
                  {{ feature.number }}
                </span>

                <span class="feature-title">
                  {{ feature.title }}
                </span>

              </button>

            </div>

          </div>


          <!-- Right -->
          <div class="feature-detail">

            <Transition name="feature-fade" mode="out-in">

              <div :key="activeFeature">

                <div class="detail-number">
                  {{ features[activeFeature].number }}
                </div>

                <h3>
                  {{ features[activeFeature].insight }}
                </h3>

                <p>
                  {{ features[activeFeature].description }}
                </p>

              </div>

            </Transition>

          </div>

        </div>

      </div>

    </section>


    <!-- =========================
         CTA
         ========================= -->

    <section class="cta-section">

      <div class="cta-content">

        <h2>
          Ready to read the fine print?
        </h2>

        <p>
          Paste your document or upload a PDF — no account needed to try it out.
        </p>

        <router-link to="/analyze" class="btn-primary">
          Start Analyzing
        </router-link>

      </div>

    </section>

  </div>
</template>


<script setup>
import { ref, onMounted, onUnmounted } from 'vue'


/* =========================
   FEATURES
   ========================= */

const activeFeature = ref(0)

const features = [
  {
    number: '01',
    title: 'Summarize lengthy agreements',
    insight: 'Plain-language overview',
    description:
      'Get the main points without reading every page of legal text.'
  },
  {
    number: '02',
    title: 'Identify privacy & data practices',
    insight: 'Know what happens to your data',
    description:
      'See what information is collected, how it is used, and whether it is shared with others.'
  },
  {
    number: '03',
    title: 'Detect concerning clauses',
    insight: 'Know what to look out for',
    description:
      'Find terms such as automatic renewal, arbitration, broad licenses, and liability limitations.'
  },
  {
    number: '04',
    title: 'Understand faster',
    insight: 'See the explanation in context',
    description:
      'Connect each AI explanation back to the original section of the document.'
  }
]


/* =========================
   DOCUMENT TYPES
   ========================= */

const documentTypes = [
  'Terms & Conditions',
  'Privacy Policy',
  'Terms of Service',
  'User Agreement',
  'Subscription Terms',
  'App Terms',
  'Website Terms',
  'Software License',
  'Refund Policy',
  'Membership Agreement',
  'Service Agreement',
  'Cookie Policy'
]


/* =========================
   SECTION SCROLLING
   ========================= */

const currentSection = ref(0)
const isScrolling = ref(false)

const easeInOutCubic = (t) => {
  return t < 0.5
    ? 4 * t * t * t
    : 1 - Math.pow(-2 * t + 2, 3) / 2
}


const animateScroll = (targetY, duration = 900) => {
  const startY = window.scrollY
  const distance = targetY - startY
  const startTime = performance.now()

  const animate = (currentTime) => {
    const elapsed = currentTime - startTime
    const progress = Math.min(elapsed / duration, 1)

    const easedProgress = easeInOutCubic(progress)

    window.scrollTo(
      0,
      startY + distance * easedProgress
    )

    if (progress < 1) {
      requestAnimationFrame(animate)
    } else {
      isScrolling.value = false
    }
  }

  requestAnimationFrame(animate)
}


const scrollToSection = (index) => {
  const sections = document.querySelectorAll('.home > section')

  if (index < 0 || index >= sections.length) {
    isScrolling.value = false
    return
  }

  currentSection.value = index
  isScrolling.value = true

  const targetY =
    sections[index].getBoundingClientRect().top + window.scrollY

  animateScroll(targetY, 700)
}


const handleWheel = (event) => {
  if (isScrolling.value) {
    event.preventDefault()
    return
  }

  if (Math.abs(event.deltaY) < 10) return

  event.preventDefault()

  if (event.deltaY > 0) {
    scrollToSection(currentSection.value + 1)
  } else {
    scrollToSection(currentSection.value - 1)
  }
}


const handleKeydown = (event) => {
  if (isScrolling.value) return

  if (
    event.key === 'ArrowDown' ||
    event.key === 'PageDown'
  ) {
    event.preventDefault()
    scrollToSection(currentSection.value + 1)
  }

  if (
    event.key === 'ArrowUp' ||
    event.key === 'PageUp'
  ) {
    event.preventDefault()
    scrollToSection(currentSection.value - 1)
  }

  if (event.key === 'Home') {
    event.preventDefault()
    scrollToSection(0)
  }

  if (event.key === 'End') {
    event.preventDefault()

    const sections = document.querySelectorAll('.home > section')

    scrollToSection(sections.length - 1)
  }
}


onMounted(() => {
  window.addEventListener(
    'wheel',
    handleWheel,
    { passive: false }
  )

  window.addEventListener(
    'keydown',
    handleKeydown
  )
})


onUnmounted(() => {
  window.removeEventListener(
    'wheel',
    handleWheel
  )

  window.removeEventListener(
    'keydown',
    handleKeydown
  )
})
</script>


<style scoped>

/* =========================
   GENERAL
   ========================= */

.home {
  width: 100%;
}


/* =========================
   HERO
   ========================= */

.hero {
  height: 100vh;
  min-height: 100vh;

  display: flex;
  align-items: center;

  padding: 80px 40px;

  background: #f1f8f5;
}

.hero-content {
  width: 100%;
  max-width: 1100px;

  margin: 0 auto;

  text-align: left;
}

.hero h1 {
  max-width: 750px;

  margin: 0 0 22px;

  font-size: 52px;
  line-height: 1.15;

  color: #2c3e50;
}

.hero p {
  max-width: 700px;

  margin: 0 0 35px;

  font-size: 20px;
  line-height: 1.7;

  color: #667085;
}

.hero-buttons {
  display: flex;
  align-items: center;

  gap: 12px;
}

.btn-primary,
.btn-secondary {
  display: inline-block;

  padding: 12px 24px;

  border-radius: 6px;

  font-weight: 600;

  text-decoration: none;

  transition: 0.2s;
}

.btn-primary {
  background: #42b883;
  color: white;
}

.btn-primary:hover {
  background: #369f6e;
}

.btn-secondary {
  background: white;
  color: #2c3e50;

  border: 1px solid #d0d5dd;
}

.btn-secondary:hover {
  background: #f8f9fa;
}


/* =========================
   WHAT YOU CAN ANALYZE
   ========================= */

.document-section {
  height: 100vh;
  min-height: 100vh;

  display: flex;
  align-items: center;

  padding: 80px 40px;

  background: #f8faf9;

  overflow: hidden;
}

.document-content {
  width: 100%;
  max-width: 1100px;

  margin: 0 auto;

  display: grid;

  grid-template-columns: 0.85fr 1.15fr;

  gap: 80px;

  align-items: center;
}


/* Left */

.document-heading {
  position: relative;
  z-index: 2;
}

.document-eyebrow {
  margin-bottom: 18px;

  font-size: 13px;
  font-weight: 700;

  letter-spacing: 0.12em;

  color: #42b883;
}

.document-heading h2 {
  max-width: 450px;

  margin: 0 0 20px;

  font-size: 46px;
  line-height: 1.15;

  color: #2c3e50;
}

.document-heading p {
  max-width: 470px;

  margin: 0;

  font-size: 19px;
  line-height: 1.7;

  color: #667085;
}


/* =========================
   PAPER PILE
   ========================= */

.document-pile {
  position: relative;

  width: 100%;
  height: 560px;

  display: flex;
  align-items: center;
  justify-content: center;
}


/* Paper */

.document-paper {
  position: absolute;

  width: 230px;
  min-height: 145px;

  padding: 25px 22px 20px;

  background: #fffefa;

  border: 1px solid #d9ddd9;

  border-radius: 2px;

  color: #344054;

  box-shadow:
    0 5px 12px rgba(44, 62, 80, 0.06),
    0 18px 35px rgba(44, 62, 80, 0.04);

  transition:
    box-shadow 0.3s ease,
    filter 0.3s ease;

  overflow: hidden;
}


/* Folded corner */

.paper-fold {
  position: absolute;

  top: -1px;
  right: -1px;

  width: 34px;
  height: 34px;

  background: #eef2ef;

  clip-path: polygon(0 0, 100% 100%, 100% 0);

  border-left: 1px solid #d9ddd9;
  border-bottom: 1px solid #d9ddd9;
}


/* Paper content */

.paper-content {
  position: relative;
  z-index: 2;
}

.paper-title {
  margin: 12px 0 15px;

  font-size: 15px;
  font-weight: 700;

  line-height: 1.35;

  color: #344054;
}


/* Fake document text */

.paper-lines {
  display: flex;
  flex-direction: column;
  gap: 5px;
}

.paper-lines span {
  display: block;

  height: 3px;

  width: 90%;

  border-radius: 2px;

  background: #e4e8e5;
}

.paper-lines span:nth-child(2) {
  width: 75%;
}

.paper-lines span:nth-child(3) {
  width: 84%;
}

.paper-lines.short span:first-child {
  width: 70%;
}

.paper-lines.short span:last-child {
  width: 45%;
}


/* Hover */

.document-paper:hover {
  z-index: 30;

  filter: brightness(1.01);

  box-shadow:
    0 10px 20px rgba(44, 62, 80, 0.10),
    0 25px 45px rgba(44, 62, 80, 0.08);
}


/* =========================
   PAPER POSITIONS
   ========================= */

.document-paper-1 {
  top: -2%;
  left: 14%;
  transform: rotate(-12deg);
  animation-delay: -0.5s;
}

.document-paper-2 {
  top: 2%;
  right: -6%;
  transform: rotate(8deg);
  animation-delay: -1.2s;
}

.document-paper-3 {
  top: 23%;
  left: -9%;
  transform: rotate(6deg);
  animation-delay: -1.9s;
}

.document-paper-4 {
  top: 18%;
  left: 31%;
  transform: rotate(-5deg);
  animation-delay: -2.6s;
}

.document-paper-5 {
  top: 27%;
  right: -8%;
  transform: rotate(-9deg);
  animation-delay: -3.3s;
}

.document-paper-6 {
  top: 44%;
  left: 3%;
  transform: rotate(10deg);
  animation-delay: -4s;
}

.document-paper-7 {
  top: 46%;
  left: 38%;
  transform: rotate(4deg);
  animation-delay: -4.7s;
}

.document-paper-8 {
  top: 52%;
  right: -2%;
  transform: rotate(-7deg);
  animation-delay: -5.4s;
}

.document-paper-9 {
  top: 72%;
  left: 16%;
  transform: rotate(9deg);
  animation-delay: -6.1s;
}

.document-paper-10 {
  top: 13%;
  right: 22%;
  transform: rotate(-7deg);
  animation-delay: -1.7s;
}

.document-paper-11 {
  top: 57%;
  left: -12%;
  transform: rotate(-8deg);
  animation-delay: -3.1s;
}

.document-paper-12 {
  top: 76%;
  right: -9%;
  transform: rotate(7deg);
  animation-delay: -5.1s;
}


/* =========================
   HOW WE WILL HELP
   ========================= */

.analyze-section {
  height: 100vh;
  min-height: 100vh;

  display: flex;
  align-items: center;

  padding: 80px 40px;

  background: white;
}

.analyze-wrapper {
  width: 100%;
  max-width: 1100px;

  margin: 0 auto;
}


/* Heading */

.section-heading {
  margin-bottom: 45px;
}

.section-heading h2 {
  margin: 0;

  color: #2c3e50;

  font-size: 48px;
  line-height: 1.15;
}

.section-line {
  width: 100%;
  height: 1px;

  margin-top: 25px;

  background: #d0d5dd;
}


/* Content */

.analyze-content {
  display: grid;

  grid-template-columns: 1fr 1fr;

  gap: 80px;

  align-items: center;
}


/* Left */

.feature-navigation {
  width: 100%;
}

.feature-list {
  display: flex;
  flex-direction: column;
}

.feature-tab {
  width: 100%;

  display: grid;

  grid-template-columns: 45px 1fr 25px;

  align-items: center;

  gap: 10px;

  padding: 28px 0;

  background: none;

  border: none;
  border-bottom: 1px solid #e5e7eb;

  text-align: left;

  cursor: pointer;

  color: #98a2b3;

  transition:
    color 0.35s ease,
    padding-left 0.35s ease;
}

.feature-tab:hover {
  color: #667085;
  padding-left: 6px;
}

.feature-tab.active {
  color: #2c3e50;
  padding-left: 14px;
}


/* Number */

.feature-number {
  font-size: 20px;
  font-weight: 600;

  color: #b0b7c3;

  transition:
    color 0.35s ease,
    transform 0.35s ease;
}

.feature-tab.active .feature-number {
  color: #42b883;

  transform: scale(1.1);
}


/* Title */

.feature-title {
  font-size: 19px;
  font-weight: 600;

  transition:
    transform 0.35s ease,
    color 0.35s ease;
}

.feature-tab.active .feature-title {
  color: #2c3e50;

  transform: scale(1.08);

  transform-origin: left center;
}


/* Arrow */

.feature-arrow {
  font-size: 22px;

  opacity: 0;

  transform: translateX(-8px);

  transition:
    opacity 0.3s ease,
    transform 0.3s ease;
}

.feature-tab:hover .feature-arrow,
.feature-tab.active .feature-arrow {
  opacity: 1;

  transform: translateX(0);
}


/* Right */

.feature-detail {
  min-height: 320px;

  display: flex;
  align-items: center;

  padding-left: 60px;

  border-left: 1px solid #d0d5dd;
}

.detail-number {
  margin-bottom: 18px;

  font-size: 20px;
  font-weight: 600;

  color: #42b883;
}

.feature-detail h3 {
  max-width: 500px;

  margin: 0 0 20px;

  font-size: 38px;
  line-height: 1.2;

  color: #2c3e50;
}

.feature-detail p {
  max-width: 500px;

  margin: 0;

  font-size: 20px;
  line-height: 1.7;

  color: #667085;
}


/* Transition */

.feature-fade-enter-active,
.feature-fade-leave-active {
  transition:
    opacity 0.35s ease,
    transform 0.35s ease;
}

.feature-fade-enter-from {
  opacity: 0;

  transform: translateX(20px);
}

.feature-fade-leave-to {
  opacity: 0;

  transform: translateX(-20px);
}


/* =========================
   CTA
   ========================= */

.cta-section {
  height: 50vh;
  min-height: 400px;

  display: flex;
  align-items: center;
  justify-content: center;

  padding: 60px 40px;

  background: #f1f8f5;

  text-align: center;
}

.cta-content {
  width: 100%;
  max-width: 800px;
}

.cta-section h2 {
  margin: 0 0 18px;

  font-size: 42px;
  line-height: 1.2;

  color: #2c3e50;
}

.cta-section p {
  margin: 0 0 28px;

  font-size: 20px;
  line-height: 1.6;

  color: #667085;
}


/* =========================
   MOBILE
   ========================= */

@media (max-width: 800px) {

  .hero,
  .document-section,
  .analyze-section {
    min-height: 100vh;
    height: auto;
  }

  .hero {
    min-height: 100vh;
  }

  .hero h1 {
    font-size: 40px;
  }

  .hero p {
    font-size: 18px;
  }


  /* Documents */

  .document-section {
    padding: 80px 25px;
  }

  .document-content {
    grid-template-columns: 1fr;

    gap: 20px;
  }

  .document-heading h2 {
    font-size: 38px;
  }

  .document-pile {
    position: relative;

    width: 110%;
    height: 580px;

    margin-left: -5%;

    display: flex;
    align-items: center;
    justify-content: center;
  }


  /* Features */

  .analyze-section {
    padding: 80px 25px;
  }

  .section-heading {
    margin-bottom: 35px;
  }

  .section-heading h2 {
    font-size: 38px;
  }

  .analyze-content {
    grid-template-columns: 1fr;

    gap: 45px;
  }

  .feature-detail {
    min-height: 250px;

    padding-left: 0;
    padding-top: 35px;

    border-left: none;
    border-top: 1px solid #d0d5dd;
  }

  .feature-detail h3 {
    font-size: 32px;
  }
}


/* =========================
   SMALL MOBILE
   ========================= */

@media (max-width: 600px) {

  .hero {
    padding: 70px 20px;
  }

  .hero h1 {
    font-size: 34px;
  }

  .hero p {
    font-size: 17px;
  }

  .hero-buttons {
    flex-direction: column;
    align-items: stretch;
  }

  .btn-primary,
  .btn-secondary {
    text-align: center;
  }


  /* Documents */

  .document-section {
    padding: 70px 20px;
  }

  .document-heading h2 {
    font-size: 34px;
  }

  .document-heading p {
    font-size: 17px;
  }

  .document-pile {
    height: 430px;
  }

  .document-paper {
    width: 175px;
    min-height: 115px;

    padding: 19px 17px 15px;
  }

  .document-paper-1 {
    left: 18%;
  }

  .document-paper-2 {
    right: 0;
  }

  .document-paper-3 {
    left: 0;
  }

  .document-paper-4 {
    left: 24%;
  }

  .document-paper-5 {
    right: 0;
  }

  .document-paper-6 {
    left: 8%;
  }

  .document-paper-7 {
    left: 30%;
  }

  .document-paper-8 {
    right: 5%;
  }

  .document-paper-9 {
    left: 15%;
  }

  .document-paper-10 {
    right: 18%;
  }

  .document-paper-11 {
    left: -3%;
  }

  .document-paper-12 {
    right: -4%;
  }

  .paper-title {
    font-size: 12px;
  }


  /* Features */

  .section-heading h2 {
    font-size: 34px;
  }

  .feature-title {
    font-size: 17px;
  }

  .feature-tab {
    grid-template-columns: 35px 1fr 20px;

    padding: 24px 0;
  }

  .feature-tab.active {
    padding-left: 8px;
  }

  .feature-tab.active .feature-title {
    transform: scale(1.04);
  }

  .feature-detail h3 {
    font-size: 28px;
  }

  .feature-detail p {
    font-size: 18px;
  }


  /* CTA */

  .cta-section {
    height: 50vh;
    min-height: 350px;

    padding: 50px 20px;
  }

  .cta-section h2 {
    font-size: 34px;
  }

  .cta-section p {
    font-size: 17px;
  }
}
</style>