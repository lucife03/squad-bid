// Initialize Bootstrap modal
const joinModal = new bootstrap.Modal(document.getElementById('joinDealModal'));
let currentDealId = null;

// Show join form modal
function showJoinForm(dealId) {
    currentDealId = dealId;
    const form = document.getElementById('joinDealForm');
    form.action = `/join-deal/${dealId}`;
    joinModal.show();
}

// Update deal status
async function updateDealStatus(dealId) {
    try {
        const response = await fetch(`/deal-status/${dealId}`);
        const data = await response.json();
        
        // Update progress bar
        const card = document.querySelector(`[data-deal-id="${dealId}"]`).closest('.card');
        const progressBar = card.querySelector('.progress-bar');
        const percentage = (data.current_participants / data.min_participants * 100).toFixed(1);
        progressBar.style.width = `${Math.min(percentage, 100)}%`;
        progressBar.textContent = `${data.current_participants}/${data.min_participants} participants`;

        // Update time remaining
        const timeElement = card.querySelector('.time-remaining');
        if (data.is_active) {
            const hours = Math.floor(data.time_remaining / 3600);
            const minutes = Math.floor((data.time_remaining % 3600) / 60);
            timeElement.textContent = `Time remaining: ${hours}h ${minutes}m`;
        } else {
            timeElement.textContent = 'Deal has expired';
            const joinButton = card.querySelector('.btn-success');
            if (joinButton) {
                joinButton.classList.replace('btn-success', 'btn-secondary');
                joinButton.disabled = true;
                joinButton.textContent = 'Expired';
            }
        }
    } catch (error) {
        console.error('Error updating deal status:', error);
    }
}

// Update all deals status periodically
function updateAllDeals() {
    const dealElements = document.querySelectorAll('[data-deal-id]');
    dealElements.forEach(element => {
        const dealId = element.dataset.dealId;
        updateDealStatus(dealId);
    });
}

// Initial update and set interval
updateAllDeals();
setInterval(updateAllDeals, 30000); // Update every 30 seconds 