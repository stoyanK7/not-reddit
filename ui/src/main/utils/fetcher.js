const fetcher = (params) => {
    const [url, headerValue] = params;
    return fetch(url, headerValue).then(res => res.json());
};

export default fetcher;
