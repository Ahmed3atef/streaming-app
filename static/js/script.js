/* ================================================================
   CineVault — Main JavaScript
   Sections:
     1. Navbar scroll effect
     2. Search overlay
     3. Toast notifications
     4. Movie player
     5. Series season tabs
     6. Browse page type filter
================================================================ */


/* ── 1. NAVBAR SCROLL EFFECT ── */
const navbar = document.getElementById('navbar');
if (navbar) {
    window.addEventListener('scroll', () => {
        navbar.classList.toggle('scrolled', window.scrollY > 40);
    });
}


/* ── 2. SEARCH OVERLAY ── */
function toggleSearch() {
    const overlay = document.getElementById('search-overlay');
    if (!overlay) return;
    const isOpen = overlay.classList.contains('open');
    overlay.classList.toggle('open', !isOpen);
    if (!isOpen) {
        const input = overlay.querySelector('.search-input');
        if (input) input.focus();
    }
}

document.addEventListener('keydown', e => {
    if (e.key === 'Escape') {
        const overlay = document.getElementById('search-overlay');
        if (overlay) overlay.classList.remove('open');
    }
});


/* ── 3. TOAST NOTIFICATIONS ── */
function showToast(msg) {
    const t = document.getElementById('toast');
    if (!t) return;
    t.textContent = msg;
    t.classList.add('show');
    setTimeout(() => t.classList.remove('show'), 3000);
}


/* ── 4. MOVIE PLAYER ── */
function startPlayer() {
    const playerSection = document.getElementById('player-section');
    if (!playerSection) return;
    playerSection.scrollIntoView({ behavior: 'smooth' });
    setTimeout(loadVideo, 600);
}

function loadVideo() {
    const placeholder = document.getElementById('player-placeholder');
    const video = document.getElementById('movie-video');
    if (placeholder && video) {
        placeholder.style.display = 'none';
        video.style.display = 'block';
        video.play();
    }
}


/* ── 5. SERIES SEASON TABS ── */
function switchSeason(index, btn) {
    document.querySelectorAll('.season-tab').forEach(t => t.classList.remove('active'));
    document.querySelectorAll('.season-panel').forEach(p => p.classList.remove('active'));
    btn.classList.add('active');
    const panel = document.getElementById('season-panel-' + index);
    if (panel) panel.classList.add('active');
}


/* ── 6. BROWSE PAGE TYPE FILTER ── */
function filterType(type, btn) {
    document.querySelectorAll('.type-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    document.querySelectorAll('.media-card[data-type]').forEach(card => {
        card.style.display = (type === 'all' || card.dataset.type === type) ? '' : 'none';
    });
}
