const { defineConfig } = require("cypress");

module.exports = defineConfig({
  e2e: {
    experimentalModifyObstructiveThirdPartyCode: true,
    baseUrl: "http://127.0.0.1:3000",
  },
});
