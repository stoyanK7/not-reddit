export default function LoadMore({ canLoadMore, page, setPage }) {
    return (
        <>
            {canLoadMore &&
                <button
                    className="w-full p-2 rounded-sm bg-reddit-orange text-white"
                    onClick={() => setPage(page + 1)}>
                    Load more
                </button>
            }
            {!canLoadMore &&
                <span>That&lsquo;s all.</span>
            }
        </>
    );
}
