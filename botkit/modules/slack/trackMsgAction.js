// Slack sometimes sends a message multiple times
// Make sure we only handle it once
// See https://stackoverflow.com/questions/50715387/slack-events-api-triggers-multiple-times-by-one-message

const msgIds = [];
const msgIdsMax = 10;

function trackMessage(msgId) {
  msgIds.push(msgId);
  // Keep the most recent N items
  if (msgIds.length > msgIdsMax) {
    msgIds.shift();
  }
}

function isMessageProcessed(msgId) {
  if (msgIds.indexOf(msgId) !== -1) {
    return true;
  }
  return false;
}

module.exports = {
  trackMessage,
  isMessageProcessed,
}
