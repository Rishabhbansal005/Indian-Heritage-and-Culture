const toggle = document.querySelector('.toggle');
const dropdownMenu = document.querySelector('.dropdownmenu');

if (toggle) {
    toggle.addEventListener('click', () => {
        dropdownMenu.classList.toggle('active');
    });
}

// Close dropdown when clicking outside
document.addEventListener('click', (e) => {
    if (toggle && dropdownMenu && !toggle.contains(e.target as Node) && !dropdownMenu.contains(e.target as Node)) {
        dropdownMenu.classList.remove('active');
    }
});


// Audio Toggle Logic
function initAudioToggle() {
    const bgMusic = document.getElementById("bg-music");

    // Create the button dynamically if it doesn't exist
    if (document.getElementById("music-toggle-btn")) return;

    const musicBtn = document.createElement("button");
    musicBtn.id = "music-toggle-btn";
    musicBtn.innerHTML = '🔊'; // Playing by default based on current HTML
    document.body.appendChild(musicBtn);

    if (bgMusic) {
        // Load the saved state or default to playing
        const isMusicPaused = localStorage.getItem("musicPaused") === "true";

        if (isMusicPaused) {
            bgMusic.autoplay = false;
            bgMusic.pause();
            musicBtn.innerHTML = '🔇';
            musicBtn.classList.add('muted');
        } else {
            // In some browsers autoplay is blocked, but we set it anyway
            bgMusic.play().catch(e => {
                console.log("Autoplay prevented by browser", e);
                musicBtn.innerHTML = '🔇';
                musicBtn.classList.add('muted');
            });
        }

        // Ensure volume is normal
        bgMusic.volume = 0.5;

        // Toggle functionality
        musicBtn.addEventListener("click", () => {
            if (bgMusic.paused) {
                bgMusic.play();
                musicBtn.innerHTML = '🔊';
                musicBtn.classList.remove('muted');
                localStorage.setItem("musicPaused", "false");
            } else {
                bgMusic.pause();
                musicBtn.innerHTML = '🔇';
                musicBtn.classList.add('muted');
                localStorage.setItem("musicPaused", "true");
            }
        });
    }
}

// Run safely after DOM is loaded across all browsers
if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initAudioToggle);
} else {
    initAudioToggle();
}
