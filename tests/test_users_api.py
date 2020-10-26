from app import exceptions
from app.core.users import User

# mocker.patch.object(model.Perilla, "get_hanged_tasks", return_value=[])

# query = mocker.patch.object(model.Task, "query")
# query.filter.return_value.first.return_value = task(status="TIMEOUTED")


class TestGETUsersResource:

    def test_get_users_returns_200_if_user_exists_in_the_db(self, mocker, test_app, user_builder):

        mocked_user = user_builder(name="foo")
        mocker.patch.object(User, "get", return_value=mocked_user)
        response = test_app.get("/users/1")
        assert response.status_code == 200
        assert response.json == mocked_user.to_dict()

    def test_get_users_returns_404_if_user_exists_in_the_db(self, mocker, test_app, user_builder):

        mocker.patch.object(User, "get", side_effect=exceptions.UserNotFoundError)
        response = test_app.get("/users/1")
        assert response.status_code == 404

    def test_get_users_returns_500_on_error_retrieving_user(self, mocker, test_app, user_builder):

        mocker.patch.object(User, "get", side_effect=exceptions.UnableToGetUserError)
        response = test_app.get("/users/1")
        assert response.status_code == 500


class TestPOSTUsersResource:

    def test_create_user_returns_201_if_user_exists_is_created_ok(self, mocker, test_app, user_builder):
        mocked_user = user_builder(name="foo")
        mocker.patch.object(User, "create", return_value=mocked_user)
        response = test_app.post("/users", json={"name": "foo"})
        assert response.status_code == 201
        assert response.json == mocked_user.to_dict()

    def test_get_users_returns_500_on_error_creating_user(self, mocker, test_app, user_builder):
        mocker.patch.object(User, "create", side_effect=exceptions.UnableToCreateUserError)
        response = test_app.post("/users", json={"name": "foo"})
        assert response.status_code == 500

    def test_get_users_returns_400_on_wrong_payload(self, mocker, test_app, user_builder):
        response = test_app.post("/users", json={"something-wrong": "foo"})
        assert response.status_code == 400


class TestPUTUsersResource:

    def test_update_user_returns_200_if_user_is_updated_ok(self, mocker, test_app, user_builder):
        mocked_user = user_builder(name="foo")
        mocker.patch.object(User, "get", return_value=mocked_user)

        mocked_user.name = "foo-new-name"
        mocker.patch.object(User, "update", return_value=mocked_user)
        response = test_app.put("/users/1", json={"name": "foo-new-name"})
        assert response.status_code == 200
        assert response.json == mocked_user.to_dict()

    def test_update_user_returns_404_if_user_to_update_does_not_exist(self, mocker, test_app, user_builder):
        mocker.patch.object(User, "get", side_effect=exceptions.UserNotFoundError)
        response = test_app.put("/users/1", json={"name": "foo-new-name"})
        assert response.status_code == 404

    def test_update_user_returns_500_on_error_updating_users(self, mocker, test_app, user_builder):
        mocker.patch.object(User, "get", side_effect=exceptions.UnableToUpdateUserError)
        response = test_app.put("/users/1", json={"name": "foo-new-name"})
        assert response.status_code == 500
