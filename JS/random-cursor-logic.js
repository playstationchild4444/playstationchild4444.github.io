const jsFiles = [
    "images/custom-cursor-bloxy.js",
    "images/custom-cursor-car.js",
];

// Function to randomly select a JavaScript file
function getRandomJsFile() {
    const randomIndex = Math.floor(Math.random() * jsFiles.length);
    return jsFiles[randomIndex];
}

// Dynamically create a script tag with the randomly selected JavaScript file
function loadRandomJsFile() {
    const script = document.createElement("script");
    script.src = getRandomJsFile();
    script.onerror = function() {
        console.error("Failed to load script:", script.src);
    };
    document.head.appendChild(script);
}

// Load the random JavaScript file when the page loads
window.addEventListener("load", loadRandomJsFile);
