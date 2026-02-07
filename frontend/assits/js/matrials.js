function updateTimeAndDate() {
        const footerTime = document.getElementById('footer_time');
        const footerDate = document.getElementById('footer_date');

        if (footerTime && footerDate) {
            const now = new Date();
            footerTime.textContent = now.toLocaleTimeString();
            footerDate.textContent = now.toLocaleDateString();
        }
    }

    // This makes it automatic every second
    setInterval(updateTimeAndDate, 1000);
    
    // Run immediately
    updateTimeAndDate();
URL("matrials.html");