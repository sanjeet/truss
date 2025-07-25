/* tslint:disable */
/* eslint-disable */

/* auto-generated by NAPI-RS */

export declare class PerformanceClient {
  constructor(baseUrl: string, apiKey?: string | undefined | null)
  embed(input: Array<string>, model: string, encodingFormat?: string | undefined | null, dimensions?: number | undefined | null, user?: string | undefined | null, maxConcurrentRequests?: number | undefined | null, batchSize?: number | undefined | null, timeoutS?: number | undefined | null, maxCharsPerRequest?: number | undefined | null, hedgeDelay?: number | undefined | null): Promise<any>
  rerank(query: string, texts: Array<string>, rawScores?: boolean | undefined | null, returnText?: boolean | undefined | null, truncate?: boolean | undefined | null, truncationDirection?: string | undefined | null, maxConcurrentRequests?: number | undefined | null, batchSize?: number | undefined | null, timeoutS?: number | undefined | null, maxCharsPerRequest?: number | undefined | null, hedgeDelay?: number | undefined | null): Promise<any>
  classify(inputs: Array<string>, rawScores?: boolean | undefined | null, truncate?: boolean | undefined | null, truncationDirection?: string | undefined | null, maxConcurrentRequests?: number | undefined | null, batchSize?: number | undefined | null, timeoutS?: number | undefined | null, maxCharsPerRequest?: number | undefined | null, hedgeDelay?: number | undefined | null): Promise<any>
  batchPost(urlPath: string, payloads: Array<JsonValue>, maxConcurrentRequests?: number | undefined | null, timeoutS?: number | undefined | null): Promise<any>
}
