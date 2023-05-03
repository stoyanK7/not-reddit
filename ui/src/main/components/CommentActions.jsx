export default function CommentActions({ votes }) {
    function upvote() {
        // TODO: implement call
        // TODO: give visual feedback
    }

    function downvote() {
        // TODO: implement call
        // TODO: give visual feedback
    }

    return (
        <div
            className="flex gap-2 text-reddit-gray hover:cursor-pointer">
            <div
                className="flex items-center">
                <span
                    className="p-2 mr-1 rounded-sm hover:bg-reddit-orange-light text-reddit-orange"
                    onClick={upvote}>
                    Up
                </span>
                <span
                    className="font-bold text-reddit-black">{votes}</span>
                <span
                    className="p-2 ml-1 rounded-sm hover:bg-reddit-blue-light text-reddit-blue"
                    onClick={downvote}>
                    Down
                </span>
            </div>
            <div
                className="p-2 rounded-sm text-yellow-600 hover:bg-yellow-300">
                Award
            </div>
        </div>
    );
}
