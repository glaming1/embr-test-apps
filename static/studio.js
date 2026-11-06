const nameInput = document.querySelector("#name");
const previewName = document.querySelector("[data-preview-name]");

if (nameInput && previewName) {
  const updatePreview = () => {
    previewName.textContent = nameInput.value.trim() || "friend";
  };

  nameInput.addEventListener("input", updatePreview);
  window.addEventListener("pageshow", updatePreview);
  updatePreview();
}
