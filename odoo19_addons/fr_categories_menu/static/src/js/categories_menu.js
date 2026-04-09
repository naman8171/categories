/** @odoo-module **/

const wrappers = document.querySelectorAll('.fr-categories-wrapper');

wrappers.forEach((wrapper) => {
    const buttons = wrapper.querySelectorAll('.fr-toolbar__button');
    const screens = wrapper.querySelectorAll('[data-screen]');

    buttons.forEach((button) => {
        button.addEventListener('click', () => {
            const target = button.dataset.view;

            buttons.forEach((btn) => btn.classList.toggle('is-active', btn === button));

            screens.forEach((screen) => {
                const shouldShow = screen.dataset.screen === target;
                screen.classList.toggle('is-hidden', !shouldShow);
            });
        });
    });
});
