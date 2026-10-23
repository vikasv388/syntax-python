
const _ = require("lodash");

function getUserData(input) {
    return _.merge({}, input);
}

const user = {
    name: "Test User",
    role: "developer"
};

console.log(getUserData(user));
