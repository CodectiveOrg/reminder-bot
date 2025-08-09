import "dotenv/config";

import { getMeApi } from "@/api/get-me.api";

import { ReminderService } from "@/services/reminder.service";

async function main(): Promise<void> {
  if (!(await checkConnection())) {
    return;
  }

  const reminderService = new ReminderService();
  reminderService.run();
}

async function checkConnection(): Promise<boolean> {
  const data = await getMeApi();

  if (!data.ok) {
    console.error(data);
    return false;
  }

  console.log("Connection is OK!");
  return true;
}

main().then();
