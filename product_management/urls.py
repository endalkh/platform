from django.urls import path

from .views import (
    ChallengeListView,
    ProductListView,
    ProductRedirectView,
    ProductSummaryView,
    ProductInitiativesView,
    ProductTreeView,
    ProductTreeInteractiveView,
    ProductAreaDetailCreateUpdateView,
    ProductIdeasAndBugsView,
    CreateProductIdea,
    UpdateProductIdea,
    ProductIdeaDetail,
    CreateProductBug,
    UpdateProductBug,
    ProductBugDetail,
    ProductChallengesView,
    ProductRoleAssignmentView,
    ChallengeDetailView,
    InitiativeDetailView,
    CapabilityDetailView,
    BountyClaimView,
    CreateProductView,
    CreateOrganisationView,
    CreateChallengeView,
    DashboardView,
    ManageBountiesView,
    UpdateChallengeView,
    DeleteChallengeView,
    UpdateProductView,
    CreateBountyView,
    UpdateBountyView,
    DeleteBountyView,
    DashboardHomeView,
    DashboardProductDetailView,
    DashboardProductChallengesView,
    DashboardProductBountiesView,
    DashboardProductChallengeFilterView,
    DashboardProductBountyFilterView,
    DashboardBountyClaimRequestsView,
    DeleteBountyClaimView,
    bounty_claim_actions,
    DashboardReviewWorkView,
    CreateInitiativeView,
    CreateCapability,
    ProductIdeaListView,
    ProductBugListView,
    DeleteAttachmentView,
)

# Developer's Note: I separated the urlpatterns because I found it convenient to do like this.
# It looked too ugly when putting every path into a single list.
#
# If a new path requires to be added, add it to their corresponding part. If it does not fit
# any of the existing groups, you can add an additional group.


# URL patterns for challenge and product list views
urlpatterns = [
    path("challenges/", ChallengeListView.as_view(), name="challenges"),
    path(
        "<str:product_slug>/challenge/create/",
        CreateChallengeView.as_view(),
        name="create-challenge",
    ),
    path(
        "<str:product_slug>/challenge/update/<int:pk>/",
        UpdateChallengeView.as_view(),
        name="update-challenge",
    ),
    path(
        "<str:product_slug>/challenge/delete/<int:pk>/",
        DeleteChallengeView.as_view(),
        name="delete-challenge",
    ),
    path(
        "<str:product_slug>/challenge/<int:challenge_id>/bounty/create/",
        CreateBountyView.as_view(),
        name="create-bounty",
    ),
    path(
        "<str:product_slug>/challenge/<int:challenge_id>/bounty/update/<int:pk>",
        UpdateBountyView.as_view(),
        name="update-bounty",
    ),
    path(
        "<str:product_slug>/challenge/<int:challenge_id>/bounty/delete/<int:pk>",
        DeleteBountyView.as_view(),
        name="delete-bounty",
    ),
    path(
        "bounty_claim/delete/<int:pk>",
        DeleteBountyClaimView.as_view(),
        name="delete-bounty-claim",
    ),
    path("products/", ProductListView.as_view(), name="products"),
    path(
        "bounty-claim/<int:pk>/",
        BountyClaimView.as_view(),
        name="bounty-claim",
    ),
    path("product/create", CreateProductView.as_view(), name="create-product"),
    path(
        "product/update/<int:pk>/",
        UpdateProductView.as_view(),
        name="update-product",
    ),
    path(
        "organisation/create",
        CreateOrganisationView.as_view(),
        name="create-organisation",
    ),
]

urlpatterns += [
    path("dashboard/", DashboardView.as_view(), name="dashboard"),
    path(
        "dashboard/home",
        DashboardHomeView.as_view(),
        name="dashboard-home",
    ),
    path(
        "dashboard/bounties",
        ManageBountiesView.as_view(),
        name="manage-bounties",
    ),
    path(
        "dashboard/bounties/bounty-requests",
        DashboardBountyClaimRequestsView.as_view(),
        name="dashboard-bounty-requests",
    ),
    path(
        "dashboard/product/<str:product_slug>/",
        DashboardProductDetailView.as_view(),
        name="dashboard-product-detail",
    ),
    path(
        "dashboard/product/<str:product_slug>/challenges/",
        DashboardProductChallengesView.as_view(),
        name="dashboard-product-challenges",
    ),
    path(
        "dashboard/product/<str:product_slug>/challenges/filter/",
        DashboardProductChallengeFilterView.as_view(),
        name="dashboard-product-challenge-filter",
    ),
    path(
        "dashboard/product/<str:product_slug>/bounties/",
        DashboardProductBountiesView.as_view(),
        name="dashboard-product-bounties",
    ),
    path(
        "dashboard/bounties/action/<int:pk>/",
        bounty_claim_actions,
        name="dashboard-bounties-action",
    ),
    path(
        "dashboard/product/<str:product_slug>/bounties/filter/",
        DashboardProductBountyFilterView.as_view(),
        name="dashboard-product-bounty-filter",
    ),
    path(
        "dashboard/product/<str:product_slug>/review-work",
        DashboardReviewWorkView.as_view(),
        name="dashboard-review-work",
    ),
]


# URL patterns for various product views
urlpatterns += [
    path(
        "<str:product_slug>/",
        ProductRedirectView.as_view(),
        name="product_detail",
    ),
    path(
        "<str:product_slug>/summary",
        ProductSummaryView.as_view(),
        name="product_summary",
    ),
    path(
        "<str:product_slug>/initiatives",
        ProductInitiativesView.as_view(),
        name="product_initiatives",
    ),
    path(
        "<str:product_slug>/challenges",
        ProductChallengesView.as_view(),
        name="product_challenges",
    ),
    path(
        "<str:product_slug>/tree",
        ProductTreeView.as_view(),
        name="product_tree",
    ),
    path(
        "<str:product_slug>/tree-interactive",
        ProductTreeInteractiveView.as_view(),
        name="product_tree_interactive",
    ),
    path(
        "product-areas",
        ProductAreaDetailCreateUpdateView.as_view(),
        name="product_area",
    ),
    path(
        "product-areas/<int:pk>",
        ProductAreaDetailCreateUpdateView.as_view(),
        name="product_area_with_pk",
    ),
    path(
        "<str:product_slug>/idea-list",
        ProductIdeaListView.as_view(),
        name="product_idea_list",
    ),
    path(
        "<str:product_slug>/bug-list",
        ProductBugListView.as_view(),
        name="product_bug_list",
    ),
    path(
        "<str:product_slug>/ideas-and-bugs",
        ProductIdeasAndBugsView.as_view(),
        name="product_ideas_bugs",
    ),
    path(
        "<str:product_slug>/ideas/new",
        CreateProductIdea.as_view(),
        name="add_product_idea",
    ),
    path(
        "<str:product_slug>/idea/<int:pk>",
        ProductIdeaDetail.as_view(),
        name="product_idea_detail",
    ),
    path(
        "<str:product_slug>/ideas/update/<int:pk>",
        UpdateProductIdea.as_view(),
        name="update_product_idea",
    ),
    path(
        "<str:product_slug>/bugs/new",
        CreateProductBug.as_view(),
        name="add_product_bug",
    ),
    path(
        "<str:product_slug>/bug/<int:pk>",
        ProductBugDetail.as_view(),
        name="product_bug_detail",
    ),
    path(
        "<str:product_slug>/bugs/update/<int:pk>",
        UpdateProductBug.as_view(),
        name="update_product_bug",
    ),
    path(
        "<str:product_slug>/people",
        ProductRoleAssignmentView.as_view(),
        name="product_people",
    ),
]

# URL patterns for initiative, capability, and challenge detail views
urlpatterns += [
    path(
        "<str:product_slug>/initiative/create",
        CreateInitiativeView.as_view(),
        name="create-initiative",
    ),
    path(
        "<str:product_slug>/initiative/<int:initiative_id>",
        InitiativeDetailView.as_view(),
        name="initiative_details",
    ),
    path(
        "<str:product_slug>/capability/create",
        CreateCapability.as_view(),
        name="create-capability",
    ),
    path(
        "<str:product_slug>/capability/<int:pk>",
        CapabilityDetailView.as_view(),
        name="capability_detail",
    ),
    path(
        "<str:product_slug>/challenge/<int:pk>",
        ChallengeDetailView.as_view(),
        name="challenge_detail",
    ),
    path(
        "attachment/delete/<int:pk>",
        DeleteAttachmentView.as_view(),
        name="delete-attachment",
    ),
]
