document.querySelector('.predict-button').addEventListener('click', () => {
    const fileInput = document.querySelector('.default-file-input');
    const formData = new FormData();
    formData.append('file', fileInput.files[0]);

    fetch('/predict', {
    method: 'POST',
    body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert(data.error);
        } else {
            document.querySelector('.leaf').textContent = data.label;
            document.querySelector('.benifits').textContent = data.benefits;
            document.querySelector('.uses').textContent = data.uses;
            document.querySelector('.bname').textContent = data.botanical_name; // Update botanical name
            document.querySelector('.habitat').textContent = data.habitat; // Update habitat
            showPopup();
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Failed to predict. Please try again.');
    });
});

const fileInput = document.querySelector('.default-file-input');
const cannotUploadMessage = document.querySelector('.cannot-upload-message');
const uploadedFile = document.querySelector('.file-block');
const fileName = document.querySelector('.file-name');
const fileSize = document.querySelector('.file-size');
const progressBar = document.querySelector('.progress-bar');
const removeFileButton = document.querySelector('.remove-file-icon');
let fileFlag = 0;

fileInput.addEventListener('click', () => {
    fileInput.value = '';
});

fileInput.addEventListener('change', () => {
    const file = fileInput.files[0];
    if (file) {
    document.querySelector('.upload-icon').textContent = 'check_circle';
    document.querySelector('.dynamic-message').textContent = 'File Dropped Successfully!';
    fileName.textContent = file.name;
    fileSize.textContent = (file.size / 1024).toFixed(1) + ' KB';
    uploadedFile.style.display = 'flex';
    progressBar.style.width = 0;
    fileFlag = 0;
    }
});

removeFileButton.addEventListener('click', () => {
    uploadedFile.style.display = 'none';
    fileInput.value = '';
    document.querySelector('.upload-icon').textContent = 'file_upload';
    document.querySelector('.dynamic-message').textContent = 'Drag & drop any file here';
});

function showPopup() {
    document.getElementById('popup-1').classList.add('active');
}

document.querySelector('.close-btn').addEventListener('click', () => {
    document.getElementById('popup-1').classList.remove('active');
});




function fetchDetails(element) {
    const leafName = element.getAttribute('data-leaf'); // Get the leaf name from the data-leaf attribute

    // Fetch details from the backend
    fetch(`/get-leaf-details?leaf=${leafName}`)
    .then(response => response.json())
    .then(data => {
    if (data.error) {
        alert(data.error); // Show error if no data is found
    } else {
        // Populate modal content with fetched data
        document.getElementById('leaf-name').textContent = data.class_name;
        document.getElementById('botanical-name').textContent = data.botanical_name;
        document.getElementById('traditional-uses').textContent = data.traditional_uses;
        document.getElementById('medicinal-benefits').textContent = data.medicinal_benefits;
        document.getElementById('habitat').textContent = data.habitat;

        // Display the modal
        document.getElementById('leafModal').style.display = 'block';
    }
    })
    .catch(error => {
        console.error('Error fetching leaf details:', error);
        alert('Failed to fetch details.');
    });
}

// Function to close the modal
function closeModal() {
    document.getElementById('leafModal').style.display = 'none';
}