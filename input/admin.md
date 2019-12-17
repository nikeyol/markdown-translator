# User and Namespace Administration Tutorial
## Tutorial Overview
This tutorial is a task-oriented guide to common user and namespace administration activities necessary to operate in the VANTIQ system. It assumes that the VANTIQ server is running and a VANTIQ organization has been configured to allow the organization administrator to login. This tutorial is intended to be used by organization and namespace administrators.

All lessons make use of the [VANTIQ IDE](../../../), VANTIQ's web-based developer toolset. The IDE has two modes of operation, Development and Operations, each of which can have multiple projects. The tasks in this tutorial use Operations mode, which is selected in the middle of the top of the page. The first three tasks involve adding new users to a VANTIQ organization, so please make sure you are logged in as Organization Administrator for those tasks. Subsequent tasks require administrative access in the namespace for which the task is targeted.

## Concepts and Terminology
A VANTIQ namespace defines an isolated environment for users of the VANTIQ system. Each namespace guarantees separation of Projects, Apps, Collaboration Types and other VANTIQ resources from all other namespaces.

From the perspective of a VANTIQ user, there are three different relationships the user can have to a namespaces:

* _Home Namespace_: this is the namespace in which the user is defined. A user has only one home namespace. Deleting a user's home namespace will delete the user as well.
* _Authorized Namespace_: a user can optionally be authorized to have access to one or more additional namespaces besides their home namespace. The namespace administrator grants a user access by invitation and by doing so also specifies the level of privilege (e.g. Administrator, Developer or User).
* _Default Namespace_: the namespace in which the user is placed at login time. The user may then select a new default namespace if that user has multiple authorized namespaces.

For this tutorial, it is helpful to think about three categories of namespaces:

* _Organization Namespace_: this is the root namespace for a VANTIQ [organization](../resourceguide/index.html#organizations). It exists to hold organization-wide VANTIQ resources, such as the users who are part of the organization and other resources that have meaning across the entire organization.
* _Developer Namespace_: this is a namespace used by a VANTIQ developer to hold the application resources that are under development. The namespace's collection of resources is loosely referred to as a VANTIQ application.
* _Application Namespace_: this is a namespace used by the organization to hold the resources of a deployed VANTIQ application. If needed, new users can be created specific to the application, homed in the application namespace.  But new namespaces cannot be created while in an application namespace.

When creating a new user in a given namespace, there are three common namespace privileges from which to select:

* _Admin_: an Administrator has the ability to create, modify and delete VANTIQ resources within the namespace. An organization administrator has the additional ability to create new namespaces and users.
* _Developer_: a Developer is a special privilege level and may only be created in the organization namespace. Developers may create new namespaces for their development projects and may grant existing users access to those namespaces. However, Developers may not create new users.  This privilege usually shows up as _Developer_ in the privilege pick-list, but when in an organization namespace, it will show as _User (Developer)_.
* _User_: a User has the ability to view but not create, modify or delete VANTIQ resources within the namespace.

The IDE allows the selection of another privilege level, _Custom_, which requires the specification of VANTIQ [profiles](../resourceguide/index.html#profiles). This privilege level is outside the scope of this tutorial.

Note: Developers can create resources in namespaces in which they are _Developer_, but not in namespaces where their privilege is _User (Developer)_.    For example, a _User (Developer)_ cannot create / update projects.  
Also, _Namespace Admin_ privilege only exists in Application Namespaces.  

## Task 1: Adding a New Administrator
The VANTIQ organization administrator has the ability to add additional administrators to the organization. To add a new user with administrator capabilities to the organization, use the **Administer** button to select **Users**:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![Users](../assets/img/admin/Users.png "Users")

Use the **Create New** icon button (small plus sign in a circle at the top, right of the _Users_ pane) to create the new user:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![NewUser](../assets/img/admin/NewUser.png "New User")

Use the **Privileges** button to select _Organization Admin_ from the _Edit Namespace Privileges_ dialog:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![UserAuths](../assets/img/admin/UserAuths.png "New User Authorization")

Use the **OK** button to save the authorization parameters. Creating a new user involves sending an invitation either via email or SMS. Use the _Invite Destination_ and _Invite Source_ fields to select how to deliver that invitation. The most convenient method is via email. Enter the email address of the person to invite in the _Invite Destination_ and select _GenericEmailSender_ as the _Invite Source_. To send an invitation via SMS, you'll have to configure an [SMS Source](../sources/sms/index.html#define-an-sms-source) before adding users.

Use the **Save Changes** icon button (down arrow at the top, right of the _User: New User_ pane) to send the invitation.

The recipient of the invitation must follow the link provided in the invitation text to authenticate. Successful authentication will create the new user in the VANTIQ system and allow that user to log in as an administrator for the organization.

## Task 2: Adding a New Developer
As previously described, a VANTIQ user assigned a _Developer_ privilege level may create and administer new namespaces within the organization but otherwise has only read-only privilege in the organization namespace.

To add a new developer, follow the instructions from the previous task, [Adding a New Administrator](./admin/index.html#task-1-adding-a-new-administrator), but select _User (Developer)_ from the _Privileges_ pull-down list in the _Edit Namespace Privileges_ dialog.

## Task 3: Adding a New User
As previously described, a VANTIQ user assigned a _User_ privilege level has the ability to view but not create, modify or delete resources within the organization namespace. However, it is also the case that the same VANTIQ user may be assigned an _Admin_ privilege level in namespaces created in the organization. (This case is described in a [following task](./admin/index.html#task-5-creating-an-application-namespace).) Such a user is typically assigned _Admin_ privilege level to administer an _Application Namespace_, as [previously described](./admin/index.html#concepts-and-terminology).

To add a new standard user, follow the instructions from the previous task, [Adding a New Administrator](./admin/index.html#task-1-adding-a-new-administrator), but select _User_ from the _Privileges_ pull-down list in the _Edit Namespace Privileges_ dialog.

## Task 4: Creating a Developer Namespace
As [previously described](./admin/index.html#concepts-and-terminology), a Developer Namespace is a namespace used by a VANTIQ developer to hold the resources that are under development. The namespace’s collection of resources is loosely referred to as a VANTIQ application.

The first step in creating a Developer Namespace is to have an organization administrator create a VANTIQ user assigned _Developer_ privilege level. Follow the steps in [Task 2](./admin/index.html#task-2-adding-a-new-developer), selecting _User (Developer)_ from the _Privileges_ pull-down list.

<a name="create_dev_namespace"></a>

Once the new developer has accepted the invitation and logs in to the VANTIQ system, the developer then creates the developer namespace. Use the **Administer** button to select **Namespaces**:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![Namespaces](../assets/img/admin/Namespaces.png "Namespaces")

Use the **Create New** icon button (small plus sign in a circle at the top, right of the _Namespaces_ pane) to create the new namespace:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![NewNamespace](../assets/img/admin/NewNamespace.png "New Namespace")

In this example, the developer is creating the "SensorDevelopment" namespace. Use the **Save Changes** icon button (down arrow at the top, right of the _Namespace: New Namespace_ pane) to create the new namespace. 

<a name="change_namespace"></a>

Once the namespace is created, the developer will likely want to switch to using the new namespace. To switch namespaces, tap the namespace name found at the top, right of the IDE title bar, next to your username; in this case the namespace name is _neworg_:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![About](../assets/img/admin/ChangeNamespaceButton.png "Change Namespace")

Clicking on _neworg_ will display the _Change Namespace_ dialog:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![ChangeNamespace](../assets/img/admin/ChangeNamespace.png "Change Namespace Dialog")

Use the _SensorDevelopment_ link to switch into the newly created namespace. Note this will cause the IDE to reload and may require the user to reauthenticate since the new namespace will have its own set of VANTIQ resources.

## Task 5: Creating an Application Namespace
As [previously described](./admin/index.html#concepts-and-terminology), an Application Namespace is a namespace used by the organization to hold the resources of a deployed VANTIQ application. An Application Namespace should be created by an organization namespace administrator (rather than a developer) since the administrator can invite both new and existing VANTIQ users into the namespace.

Use the **Administer** button to select **Namespaces**:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![Namespaces](../assets/img/admin/Namespaces.png "Namespaces")

Use the **Create New** icon button (small plus sign in a circle at the top, right of the _Namespaces_ pane) to create the new namespace:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![NewAppNamespace](../assets/img/admin/NewAppNamespace.png "New App Namespace")

In this example, the administrator is creating the "SensorApp" namespace.

The administrator must then choose to either self-assign the administrator role of the new namespace or to assign the administrator role to another new or existing VANTIQ user.

* When self-assigning, simply check the _Make Me The Administrator_ checkbox.
* When delegating the administrator role to another new or existing VANTIQ user, this involves sending an invitation either via email or SMS. Use the _Invite Destination_ and _Invite Source_ fields to select how to deliver that invitation. The most convenient method is via email. Enter the email address of the person to invite in the _Invite Destination_ and select _GenericEmailSender_ as the _Invite Source_. To send an invitation via SMS, you'll have to configure an [SMS Source](../sources/sms/index.html#define-an-sms-source) before inviting the user.

Use the **Save Changes** icon button (down arrow at the top, right of the _Namespace: New Namespace_ pane) to create the new namespace.

## Task 6: Inviting Users to a Namespace
Once a namespace has been created by either an organization administrator or a developer, that namespace's administrator may authorize other users to use that namespace. If the namespace is a Developer namespace, only existing users may be authorized. If the namespace is an Organization or Application namespace, both new and existing users may be authorized.

To authorize a user to use the existing namespace, first use the **Administer** button to select **Namespaces**:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![Namespaces](../assets/img/admin/Namespaces.png "Namespaces")

then tap the target namespace link to display the _Namespace Properties_ pane:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![AuthUserToNamespace](../assets/img/admin/AuthUserToNamespace.png "Auth User to Namespace")

then tap the _Manage Authorizations_ link to display the _Edit Authorized Users_ dialog:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![EditAuthUsers](../assets/img/admin/EditAuthUsers.png "Edit Auth Users")

then tap the **Authorize User** button to display the _Send Invite_ dialog:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![SendInvite](../assets/img/admin/SendInvite.png "Send Invite")

As previously described, use the _Invite Destination_ and _Invite Source_ fields to send the invitation. Use the _Privileges_ pull-down list to select the privilege level the user is given when using the namespace. Finally, use the **Send Invite** button to send the invitation.

## Task 7: Revoking a User's Access to a Namespace
The administrator of a namespace may wish to revoke a user's access to the namespace for any reason. To revoke access, first use the **Administer** button to select **Namespaces**:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![Namespaces](../assets/img/admin/Namespaces.png "Namespaces")

then tap the target namespace link to display the _Namespace Properties_ pane:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![AuthUserToNamespace](../assets/img/admin/AuthUserToNamespace.png "Auth User to Namespace")

then tap the _Manage Authorizations_ link to display the _Edit Authorized Users_ dialog:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![EditAuthUsers](../assets/img/admin/EditAuthUsers.png "Edit Auth Users")

Find the name of the user to revoke then use the _Revoke Access_ icon button in the _Actions_ menu to finish the revocation process.

## Task 8: Changing a User's Privilege Level for a Namespace
The administrator of a namespace may wish to change a user's privilege level for the namespace. To change the privilege level, first use the **Administer** button to select **Users**:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![Users](../assets/img/admin/Users.png "Users")

then tap the target user link to display the _User_ pane:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![ChangeUser](../assets/img/admin/ChangeUser.png "Change User")

then use the **Privileges** button to select the new privilege level from the _Edit Namespace Privileges_ dialog:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![UserAuths](../assets/img/admin/UserAuths.png "New User Authorization")

Use the **OK** button to save the new user privileges, then use the **Save Changes** icon button (down arrow at the top, right of the _User: username_ pane) to save the user parameters.
