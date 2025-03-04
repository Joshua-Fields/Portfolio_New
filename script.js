document.addEventListener("DOMContentLoaded", async () => {
    gsap.from(".animated-text", { opacity: 0, y: -50, duration: 1.5 });

    // Initialize tsParticles with background mask effect
    await tsParticles.load("tsparticles", {
        fullScreen: { enable: true },
        background: {
            image: "url('/static/img/Graphic.jpg')",
            position: "center center",
            size: "cover",
            repeat: "no-repeat"
        },
        backgroundMask: {
            enable: true,
            cover: {
                color: { value: "#000000" },
                opacity: 100
            }
        },
        particles: {
            number: { value: 250 },
            color: { value: "#ffffff" },
            shape: { type: "circle" },
            opacity: { value: 1 },
            size: { value: 5, random: true },
            move: {
                enable: true,
                speed: 1.5,
                direction: "none",
                outModes: { default: "out" }
            }
        },
        interactivity: {
            events: {
                onHover: { enable: true, mode: "bubble" }, // Enable hover effect
                onClick: { enable: true, mode: "repulse" }
            },
            modes: {
                bubble: {
                    distance: 50, // Reduce distance for better interaction
                    size: 25,
                    duration: 0.4,
                    opacity: 0.6
                },
                repulse: {
                    distance: 300,
                    duration: 10
                }
            }
        },
        detectRetina: true
    });
});
