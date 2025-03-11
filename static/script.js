document.addEventListener("DOMContentLoaded", async () => {
    gsap.from(".animated-text", { opacity: 0, y: -50, duration: 1.5 });

    // Observer for Stripes Animation
    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                document.querySelectorAll('.stripe').forEach(stripe => {
                    stripe.classList.add("animated"); // Apply animation dynamically
                });
            }
        });
    }, { threshold: 0.3 });

    observer.observe(document.querySelector("#contact"));

    // Main tsParticles Effect (Full-Screen)
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
                opacity: 1
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
                onHover: { enable: true, mode: "bubble" },
                onClick: { enable: true, mode: "repulse" }
            },
            modes: {
                bubble: {
                    distance: 50,
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


    // Second tsParticles Effect (Projects Section Only)
    await tsParticles.load("projects-particles", {
        fullScreen: { enable: false }, // Only runs inside the projects div
        background: {
            image: "linear-gradient(rgba(62, 217, 234, 0.6), rgba(62, 217, 234, 0.6)), url('/static/img/Graphic.jpg')",
            position: "center center",
            size: "cover",
            repeat: "no-repeat"

        },
        backgroundMask: {
            enable: true,
            cover: {
                color: { value: "#000000" },
                opacity: 1
            }
        },
        particles: {
            number: { value: 5000 }, // Lower count for better performance
            color: { value: "#3ED9EA" }, // Teal-colored particles
            shape: { type: "circle" },
            opacity: { value: 1 },
            size: { value: 1, random: true },
            move: {
                enable: true,
                speed: 1,
                direction: "none",
                outModes: { default: "bounce" } // Makes particles bounce inside the section
            }
        },
        interactivity: {
            events: {
                onHover: { enable: true, mode: "repulse" },
                onClick: { enable: true, mode: "bubble" }
            },
            modes: {
                repulse: {
                    distance: 75,
                    duration: 15,
                    easing: "ease-out" // Gives a natural slow-down effect
                },
                bubble: {
                    distance: 60,
                    size: 20,
                    duration: 0.3,
                    opacity: 0.6
                }
            }
        },
        detectRetina: true
    });

    // Third tsParticles Effect (Contact Section Only)
    await tsParticles.load("contact-particles", {
        fullScreen: { enable: false }, // Only runs inside the projects div
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
                opacity: 1
            }
        },
        particles: {
            number: { value: 300 }, // Lower count for better performance
            color: { value: "#3ED9EA" }, // Teal-colored particles
            shape: { type: "square" },
            opacity: { value: 1 },
            size: { value: 10, random: true },
            move: {
                enable: true,
                speed: 1,
                direction: "none",
                outModes: { default: "bounce" } // Makes particles bounce inside the section
            }
        },
        interactivity: {
            events: {
                onHover: { enable: true, mode: "repulse" },
                onClick: { enable: true, mode: "bubble" }
            },
            modes: {
                repulse: {
                    distance: 75,
                    duration: 15,
                    easing: "ease-out" // Gives a natural slow-down effect
                },
                bubble: {
                    distance: 60,
                    size: 20,
                    duration: 0.3,
                    opacity: 0.6
                }
            }
        },
        detectRetina: true
    });

    await tsParticles.load("contact-particles", {
        fullScreen: { enable: false }, // Only runs inside the projects div
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
                opacity: 1
            }
        },
        particles: {
            number: { value: 300 }, // Lower count for better performance
            color: { value: "#3ED9EA" }, // Teal-colored particles
            shape: { type: "square" },
            opacity: { value: 1 },
            size: { value: 10, random: true },
            move: {
                enable: true,
                speed: 1,
                direction: "none",
                outModes: { default: "bounce" } // Makes particles bounce inside the section
            }
        },
        interactivity: {
            events: {
                onHover: { enable: true, mode: "repulse" },
                onClick: { enable: true, mode: "bubble" }
            },
            modes: {
                repulse: {
                    distance: 75,
                    duration: 15,
                    easing: "ease-out" // Gives a natural slow-down effect
                },
                bubble: {
                    distance: 60,
                    size: 20,
                    duration: 0.3,
                    opacity: 0.6
                }
            }
        },
        detectRetina: true
    });

    await tsParticles.load("contact-particles1", {
        fullScreen: { enable: false }, // Only runs inside the projects div
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
                opacity: 1
            }
        },
        particles: {
            number: { value: 300 }, // Lower count for better performance
            color: { value: "#3ED9EA" }, // Teal-colored particles
            shape: { type: "square" },
            opacity: { value: 1 },
            size: { value: 10, random: true },
            move: {
                enable: true,
                speed: 1,
                direction: "none",
                outModes: { default: "bounce" } // Makes particles bounce inside the section
            }
        },
        interactivity: {
            events: {
                onHover: { enable: true, mode: "repulse" },
                onClick: { enable: true, mode: "bubble" }
            },
            modes: {
                repulse: {
                    distance: 75,
                    duration: 15,
                    easing: "ease-out" // Gives a natural slow-down effect
                },
                bubble: {
                    distance: 60,
                    size: 20,
                    duration: 0.3,
                    opacity: 0.6
                }
            }
        },
        detectRetina: true
    });

});
