module.exports = {
  content: ["./templates/**/*.{html,j2}"],
  theme: {
    extend: {},
  },
  plugins: [require("@tailwindcss/forms")],
};
