import type { ResponseDto } from "@/dto/response/response.dto.ts";

export async function richFetch<TResult = void>(
  input: string | URL | globalThis.Request,
  init?: RequestInit,
): Promise<ResponseDto<TResult>> {
  const [response, data] = await tryToFetch<TResult>(input, init);

  if (!response.ok) {
    if (!data.ok) {
      console.error(data.description);
    } else {
      console.error(response.statusText);
    }
  }

  return data;
}

export async function tryToFetch<TResult = void>(
  input: string | URL | globalThis.Request,
  init?: RequestInit,
): Promise<[Response, ResponseDto<TResult>]> {
  if (!init) {
    init = {};
  }

  init = {
    credentials: "include",
    ...init,
  };

  if (typeof init.body === "string") {
    init.headers = {
      "Content-Type": "application/json",
      ...init.headers,
    };
  }

  const response = await fetch(`${process.env.API_BASE_URL}/${input}`, init);

  const data = (await response.json()) as ResponseDto<TResult>;

  return [response, data];
}
