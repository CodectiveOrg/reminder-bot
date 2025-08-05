import { GetMeResponseDto } from "@/dto/response/get-me.response.dto";

import { richFetch } from "@/utils/fetch.utils";

export async function getMeApi() {
  return richFetch<GetMeResponseDto>("getMe");
}
