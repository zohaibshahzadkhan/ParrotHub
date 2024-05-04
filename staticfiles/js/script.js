(function () {
  'use strict'

  // Fetch all the forms we want to apply custom Bootstrap validation styles to
  var forms = document.querySelectorAll('.needs-validation')

  // Loop over them and prevent submission
  Array.prototype.slice.call(forms)
    .forEach(function (form) {
      form.addEventListener('submit', function (event) {
        if (!form.checkValidity()) {
          event.preventDefault()
          event.stopPropagation()
        }

        form.classList.add('was-validated')
      }, false)
    })
})()

/**
 * Adds an event listener to the document to display a welcome message modal when the DOM content is loaded.
 * Checks if the welcome message has been shown before using a cookie.
 * If the welcome message has not been shown, creates and displays a modal with a welcome message for ParrotHub.
 * Sets a cookie to prevent the welcome message from showing again for a specified duration.
 * 
 * @function displayWelcomeMessage
 */
document.addEventListener("DOMContentLoaded", function () {
  /**
   * Displays a welcome message modal for ParrotHub if it has not been shown before.
   * Sets a cookie to prevent the modal from showing again for a specified duration.
   * 
   * @function displayWelcomeMessage
   */
  function displayWelcomeMessage() {
    var hasSeenWelcomeMessage = document.cookie.includes("parrothub_welcome_shown=true");
    if (!hasSeenWelcomeMessage) {
      var modalWrapper = document.createElement("div");
      modalWrapper.innerHTML = `
              <div class="modal fade" id="welcomeModal" tabindex="-1" aria-labelledby="welcomeModalLabel" aria-hidden="true">
                  <div class="modal-dialog modal-dialog-centered modal-lg">
                      <div class="modal-content">
                          <div class="modal-header">
                              <h5 class="modal-title" id="welcomeModalLabel">Welcome to ParrotHub!</h5>
                              <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                          </div>
                          <div class="modal-body">
                              <p>ParrotHub is a platform for parrot enthusiasts to discover parrots mutations, find about Events, and learn about these amazing birds.</p>
                          </div>
                      </div>
                  </div>
              </div>
          `;
      document.body.appendChild(modalWrapper);
      var welcomeModal = new bootstrap.Modal(document.getElementById('welcomeModal'), { backdrop: 'static', keyboard: false });
      welcomeModal.show();
      setTimeout(function () {
        welcomeModal.hide();
        document.cookie = "parrothub_welcome_shown=true; max-age=86400";
      }, 10000);
    }
  }
  displayWelcomeMessage();
});