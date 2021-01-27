from exe import PROJECT
from modules.others.configure import get_languages
from modules.others.my_exceptions import KnowUnknownJsonError, NotTargetSubProjectException, SelfReviewFoundException
from modules.review.GerritController import QueryBase
from modules.review.utils import remove_bots_message, extract_inline_comments_number

def extract(x):
    try:
        return int(x['_revision_number'])
    except Exception:
        return 0

class Review:
    def __init__(self, query: QueryBase, review_id, revision_info):
        self.query = query
        if type(revision_info)==list:
            revision_info = revision_info[0]
        tmp = revision_info['project'].split("/")
        if not len(tmp) == 2:
            raise NotTargetSubProjectException
        self.project = tmp[0]
        self.sub_project = tmp[1]
        if not self.is_target_sub_project(query):
            raise NotTargetSubProjectException
        review_info = query.get_review_data()
        self.total_revisions = query.get_last_diff_no()  # その変更のパッチ総数．
        self.review_id = review_id

        self.target_languages = get_languages(self.project, self.sub_project)
        self.change_id = revision_info["change_id"]
        self.status = revision_info["status"]
        self.commit_message = revision_info["subject"]
        # review_info
        # print("review_info ", review_info["messages"])
        self.comments = remove_bots_message(review_info["messages"], query.bots)
        self.total_inline_comments = extract_inline_comments_number(self.comments)
        self.total_comments = len(self.comments)  # self.total_outline_comments + self.total_inline_comments
        self.owner = review_info["owner"]["_account_id"]
        self.reviewers = set()
        for c in self.comments:
            reviewer = c['author']['_account_id']
            if not self.owner == reviewer:
                self.reviewers.add(reviewer)
        self.total_reviewers = len(self.reviewers)
        if self.total_reviewers == 0:
            raise SelfReviewFoundException


    def get_info(self):
        out = dict()
        # リビジョン数
        out["revisions"] = self.total_revisions
        # コメント数
        out["comments"] = self.total_comments
        # インラインコメント数
        out["inline_comments"] = self.total_inline_comments
        # レビュー状態
        out["status"] = self.status
        # レビュー状態（false/true）
        out["is_accepted"] = (self.status == "MERGED")
        # url
        out["url"] = self.query.get_url()
        # コミットメッセージ
        out["commit_message"] = self.commit_message
        return out

    def is_target_sub_project(self, query):
        if not self.project == query.name:
            return False
        if not (self.sub_project in PROJECT["sub_projects"]):
            return False
        return True
