export type ResponseDto<TResult = void> =
  | (TResult extends void
      ? { ok: true; result?: undefined }
      : { ok: true; result: TResult })
  | { ok: false; error_code: number; description: string };
