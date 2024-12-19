// Make dialogs draggable
// This is a modified version of the code from https://github.com/vuetifyjs/vuetify/issues/4058#issuecomment-450636420
// In particular, the reliance on setInterval has been removed in favor of a ResizeObserver

function makeDialogsDraggable() {
  const d = {};
  document.addEventListener("mousedown", e => {
    const classList = e.target.classList;
    if (!(classList.contains("v-toolbar__content") || classList.contains("v-toolbar__title"))) return;
    const closestDialog = e.target.closest(".v-dialog.v-dialog--active");
    if (e.button === 0 && closestDialog != null) { // element which can be used to move element
      const boundingRect = closestDialog.getBoundingClientRect();
      d.el = closestDialog; // element which should be moved
      d.title = e.target;
      d.mouseStartX = e.clientX;
      d.mouseStartY = e.clientY;
      d.elStartX = boundingRect.left;
      d.elStartY = boundingRect.top;
      d.el.style.position = "fixed";
      d.el.style.margin = 0;
      d.oldTransition = d.el.style.transition;
      d.el.style.transition = "none";
      d.title.classList.add("dragging");
      d.overlays = document.querySelectorAll(".v-overlay.v-overlay--active");
      d.overlays.forEach(overlay => overlay.style.display = "none");
    }
  });
  document.addEventListener("mousemove", e => {
      if (d.el === undefined) return;
      const boundingRect = d.el.getBoundingClientRect();
      d.el.style.left = Math.min(
          Math.max(d.elStartX + e.clientX - d.mouseStartX, 0),
          window.innerWidth - boundingRect.width
      ) + "px";
      d.el.style.top = Math.min(
          Math.max(d.elStartY + e.clientY - d.mouseStartY, 0),
          window.innerHeight - boundingRect.height
      ) + "px";
  });
  document.addEventListener("mouseup", () => {
      if (d.el === undefined) return;
      d.el.style.transition = d.oldTransition;
      d.el = undefined;
      d.title.classList.remove("dragging");
      d.overlays.forEach(overlay => overlay.style.display = '');
  });
  
  // If the window changes size, the dialog may be partially/completely out of bounds
  // We fix that here
  const resizeObserver = new ResizeObserver(entries => {
    entries.forEach(entry => {
      const dialogs = entry.target.querySelectorAll(".v-dialog.v-dialog--active");
      dialogs.forEach(dialog => {
        const boundingRect = dialog.getBoundingClientRect();
        dialog.style.left = Math.min(parseInt(dialog.style.left), window.innerWidth - boundingRect.width) + "px";
        dialog.style.top = Math.min(parseInt(dialog.style.top), window.innerHeight - boundingRect.height) + "px";
      });
    });
  });
  resizeObserver.observe(document.body);
}

console.warn("Going to call makeDialogsDraggable");
makeDialogsDraggable();
