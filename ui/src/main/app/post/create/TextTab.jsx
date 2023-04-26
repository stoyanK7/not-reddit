export default function TextTab({success, setBody}) {
    return (
        <>
            <textarea
                className="border border-reddit-postline rounded-sm p-2 w-full"
                placeholder="Text (optional)"
                onChange={e => setBody(e.currentTarget.value)}
                rows={6}
                disabled={success}/>
        </>
    )
}
