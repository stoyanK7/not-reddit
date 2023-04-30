export default function fromApi(endpoint) {
    return `${process.env.NEXT_PUBLIC_API_SERVICE_URL}${endpoint}`;
}
