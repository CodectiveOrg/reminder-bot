import "dotenv/config";

import { getMeApi } from "@/api/get-me.api";

async function main(): Promise<void> {
  const data = await getMeApi();
  console.log(data);
}

main().then();
