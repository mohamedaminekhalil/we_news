function handleBookClick(btn) {
    const icon = btn.querySelector('i');
    articleId = btn.id.replace("-book", "")
    if (icon.classList.contains('bi-book')) {
        icon.classList.replace('bi-book', 'bi-book-fill');
        toggleLater(articleId)
    } else {
        icon.classList.replace('bi-book-fill', 'bi-book');
        toggleLater(articleId)
    }
}

function handleBookmarkClick(btn) {
    const icon = btn.querySelector('i');
    articleId = btn.id.replace("-bookmark", "")
    if (icon.classList.contains('bi-bookmark-plus')) {
        icon.classList.replace('bi-bookmark-plus', 'bi-bookmark-fill');
        toggleSaved(articleId);
    } else {
        icon.classList.replace('bi-bookmark-fill', 'bi-bookmark-plus');
        toggleSaved(articleId);
    }
}

function toggleSaved(articleId) {
    fetch(`/toggle_saved/${articleId}`, { method: "POST" })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                // Toggle the appearance of the button (you can implement this part)
                // For example, change the button's class or icon based on the response.
            } else {
                console.error("Error toggling saved status.");
            }
        })
        .catch(error => {
            console.error("An error occurred during the AJAX request:", error);
        });
}

function toggleLater(articleId) {
    fetch(`/toggle_later/${articleId}`, { method: "POST" })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                // Toggle the appearance of the button (you can implement this part)
                // For example, change the button's class or icon based on the response.
            } else {
                console.error("Error toggling saved status.");
            }
        })
        .catch(error => {
            console.error("An error occurred during the AJAX request:", error);
        });
}

// Get all the buttons with the 'category-button' class
const buttons = document.querySelectorAll('.category-button');

let lastClickedButton = document.querySelector('[disabled]'); // Initialize the lastClickedButton to the initially disabled button

// Function to disable a button
function disableButton(button) {
  button.disabled = true;
}

// Function to enable a button
function enableButton(button) {
  button.disabled = false;
}

// Add click event listener to each button
buttons.forEach(button => {
  button.addEventListener('click', () => {
    // If there was a previously clicked button and it's not the same as the current button, enable it
    if (lastClickedButton && lastClickedButton !== button) {
      enableButton(lastClickedButton);
    }

    // Call the Python function or perform any other action here
    const category = button.dataset.category;
    console.log(`Button for ${category} clicked!`);

    // Disable the clicked button and update the lastClickedButton variable
    disableButton(button);
    lastClickedButton = button;
  });
});

function showSection(category) {
        // Hide all sections first
        const sections = document.querySelectorAll('section');
        sections.forEach(section => {
            section.style.display = 'none';
        });

        // Show the selected section
        const selectedSection = document.getElementById(category);
        selectedSection.style.display = 'block';

    }

window.onload = function () {
        const businessSection = document.getElementById('business');
        businessSection.style.display = 'block';
};