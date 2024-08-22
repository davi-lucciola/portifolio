// Navbar Transparency On Top
const headerStyleClasses = ['bg-dark', 'border-bottom', 'border-primary', 'border-5'];

function transparentHeaderOnScroll() {
  const header = document.querySelector('header');
  
  headerStyleClasses.forEach((styleClass) => {
    header.classList.toggle(styleClass, window.scrollY > 0)
  })
}

window.addEventListener('scroll', transparentHeaderOnScroll)

// Disable Scroll Snap to Smooth Scroll with OffCanvas
const offcanvas = document.getElementById('offcanvasNavbar');

offcanvas.addEventListener('show.bs.offcanvas', () => {
  const html = document.querySelector('html')
  html.classList.add('no-scroll-snap');
});

offcanvas.addEventListener('hidden.bs.offcanvas', () => {
  const html = document.querySelector('html')

  const timeInMileseconds = 500; // 0.5 seconds
  setTimeout(() => html.classList.remove('no-scroll-snap'), timeInMileseconds);
});