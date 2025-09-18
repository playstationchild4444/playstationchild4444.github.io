let spaceCount = 0;
let timeout;

document.addEventListener("keydown", (event) => {
    if (event.key === "6") {
        spaceCount++;
        clearTimeout(timeout);

        if (spaceCount === 3) {
            window.open("jambo.html", "_blank");
            spaceCount = 0; // Reset the count
        }

        timeout = setTimeout(() => {
            spaceCount = 0;
        }, 1000);
    }
});
