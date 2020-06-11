const users = {};
const expireTime = 180000; // Milliseconds after which the user should be forgotten

// When did the user do the action?
function lastAction(userId) {
  if (userId in users) {
    // Return in seconds
    return users[userId];
  }
  return null; // User never did it, or did it too long ago
}

function trackAction(userId) {
  users[userId] = Date.now();
  expireUsers();
}

// Remove users from tracking if their actions were too long ago
function expireUsers() {
  for (const userId in users) {
    if (users[userId] < Date.now() - expireTime) {
      delete users[userId];
    }
  }
}

module.exports = {
  trackAction,
  lastAction,
}
