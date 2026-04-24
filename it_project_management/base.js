
const hamburger = document.getElementById('menuHamburger');
            const panelClose = document.getElementById('panelClose');
            const overlay = document.getElementById('menuOverlay');
            const navPanel = document.getElementById('navPanel');

            function openMenu() {
                navPanel.classList.add('open');
                overlay.style.display = 'block';
                requestAnimationFrame(() => overlay.style.opacity = '1');
            }
            function closeMenu() {
                navPanel.classList.remove('open');
                overlay.style.opacity = '0';
                setTimeout(() => overlay.style.display = 'none', 300);
            }

            hamburger.addEventListener('click', openMenu);
            panelClose.addEventListener('click', closeMenu);
            overlay.addEventListener('click', closeMenu);

