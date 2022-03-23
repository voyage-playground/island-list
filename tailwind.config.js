module.exports = {
  content: ["./lib/templates/**/*.{html,j2}"],
  theme: {
    extend: {},
  },
  plugins: [require("@tailwindcss/forms")],
};
